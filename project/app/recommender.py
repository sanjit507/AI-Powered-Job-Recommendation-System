from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist
from .models import UserProfile, Job
import time  # For timing

# Initialize model
model = SentenceTransformer("Job-Rec-v1")

# Cache keys
JOBS_CACHE_KEY = "cached_job_embeddings"
FAISS_INDEX_KEY = "faiss_index"

def get_user_profile(user_id):
    """Fetch the user profile for a given user ID."""
    try:
        return UserProfile.objects.get(user_id=user_id)
    except ObjectDoesNotExist:
        raise ValueError(f"No UserProfile found for user with ID {user_id}")

def get_job_embeddings():
    """
    Precompute and cache job embeddings for faster recommendations.
    Uses the same model used for encoding user profiles.
    """
    cached_data = cache.get(JOBS_CACHE_KEY)
    faiss_index = cache.get(FAISS_INDEX_KEY)

    if cached_data and faiss_index:
        return cached_data['embeddings'], cached_data['jobs'], faiss_index

    jobs = list(Job.objects.all())
    if not jobs:
        raise ValueError("No jobs available in the database.")

    job_texts = [f"{job.location or ''} {job.category or ''} {' '.join(job.required_skills or [])}" for job in jobs]
    job_embeddings = model.encode(job_texts, convert_to_numpy=True)

    dimension = job_embeddings.shape[1]
    faiss_index = faiss.IndexFlatL2(dimension)
    faiss_index.add(job_embeddings.astype(np.float32))

    cache.set(JOBS_CACHE_KEY, {'embeddings': job_embeddings, 'jobs': jobs}, timeout=86400)
    cache.set(FAISS_INDEX_KEY, faiss_index, timeout=86400)

    return job_embeddings, jobs, faiss_index

def get_content_based_recommendations(user_id):
    """
    Generate job recommendations for a user using FAISS for fast search.
    Displays similarity scores and performance timing metrics.
    """
    start_total = time.time()

    # Step 1: Fetch user profile
    user_profile = get_user_profile(user_id)

    # Step 2: Get job embeddings and FAISS index
    job_embeddings, jobs, faiss_index = get_job_embeddings()

    # Step 3: Prepare user input
    user_text = f"{user_profile.location or ''} {user_profile.category or ''} {' '.join(user_profile.skills or [])}"

    # Time embedding generation
    start_embed = time.time()
    user_embedding = model.encode([user_text], convert_to_numpy=True)
    end_embed = time.time()

    # Time FAISS search
    start_search = time.time()
    distances, indices = faiss_index.search(user_embedding.astype(np.float32), k=5)
    end_search = time.time()

    # Convert results
    top_indices = indices[0].tolist()
    top_jobs = [jobs[i] for i in top_indices]
    similarity_scores = [1 - (dist / 2) for dist in distances[0]]  # Approximate cosine-like score

    end_total = time.time()

    # Log timing metrics and results
    print("\n🔍 Recommendation Timing Metrics:")
    print(f"User Embedding Generation: {end_embed - start_embed:.4f} seconds")
    print(f"FAISS Search (Top 5): {end_search - start_search:.6f} seconds")
    print(f"Total Time: {end_total - start_total:.4f} seconds\n")

    print("🎯 Recommended Jobs and Similarity Scores:")
    for job, score in zip(top_jobs, similarity_scores):
        print(f"Job: {job.title}, Similarity Score: {score:.2f}")

    return top_jobs