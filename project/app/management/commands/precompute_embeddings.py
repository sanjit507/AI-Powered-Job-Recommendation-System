from django.core.management.base import BaseCommand
from app.helper import precompute_job_embeddings

class Command(BaseCommand):
    help = 'Precompute BERT embeddings for all jobs'

    def handle(self, *args, **kwargs):
        self.stdout.write("Precomputing job embeddings...")
        precompute_job_embeddings()
        self.stdout.write(self.style.SUCCESS("Job embeddings precomputed successfully."))