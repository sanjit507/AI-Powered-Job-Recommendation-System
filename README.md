Project Title
An End-to-End AI Platform for Smart Recruitment
Integrating Job Recommendation, Resume Building, and Interview Assistance, Meeting Platform

📌 Project Overview
This platform revolutionises traditional recruitment by leveraging AI to streamline the entire hiring lifecycle. It connects job seekers with relevant opportunities, automates resume creation, offers interview preparation, and facilitates seamless video interviews—all in one place.

Key Problems Solved:

Inefficient job-candidate matching

Time-consuming resume building

Lack of interview preparation tools

Fragmented communication between recruiters and candidates

✨ Features
1. BERT-Based Job Recommendation Engine
How it works: Uses fine-tuned BERT to match user profiles (skills, education, preferences) with job listings via semantic analysis.

Performance: 85.17% accuracy in job-candidate matching.

2. AI-Powered Resume Builder
How it works: Generates professional resumes using Google Gemini API by analyzing user inputs (skills, experience, education).

Output: Tailored, ATS-friendly resumes in customizable templates.

3. GPT-Style Interview Assistant
How it works: Trained on datasets (HR, technical, behavioral Q&A) to simulate interviews and provide feedback.

Performance: 98.88% accuracy in generating relevant questions.

4. Interview Scheduling & Video Conferencing
Features:

Schedule interviews with calendar integration.

Secure video calls with screen sharing, chat, and recording.

Real-time coding environment for technical assessments.

⚙️ Tech Stack
Backend
Languages: Python, Node.js

Frameworks: Django, Express.js

Databases: SQLite, MongoDB

Frontend
React.js, Tailwind CSS, Redux,HTML,CSS,JavaScripts

AI/ML
Models: BERT (Hugging Face Transformers), Custom GPT-style Transformer

Libraries: TensorFlow, Keras, scikit-learn, FAISS, NLTK

APIs & Services
Google Gemini API, Google Meet API, Clerk (authentication), Convex (backend)

🚀 Installation & Setup
Prerequisites
Python 3.8+, Node.js 16+, pip, npm

cd backend  
pip install -r requirements.txt  
python manage.py migrate  
python manage.py runserver  

🖥️ Usage
For Job Seekers
Sign Up: Create a profile with skills, education, and preferences.

Get Recommendations: View AI-curated job listings.

Build Resume: Use the AI builder to generate/edit resumes.

Practice Interviews: Chat with the AI assistant.

Attend Interviews: Join video calls via shared links.

For Recruiters
Register Company: Request admin access via email.

Post Jobs: Add listings via the admin dashboard.

Review Applications: Track status (Pending → Accepted/Rejected).

Schedule Interviews: Send automated invites with video links.

📊 Performance Metrics
Component	Accuracy	Dataset Size
Job Recommendation (BERT)	85.17%	27,000 entries
Interview Assistant (GPT)	98.88%	Custom text data

👥 Team Contributions

Member	Role
Sanjit Chaudhary	Job Recommendation & Interview Assistant
Hemant Patel	AI Resume Builder
Vikram Kumar & Ayaz	Interview Application

Project Guide: Dr. Sakshiwala (Asst. Prof., NCE Chandi)

🔮 Future Work
Upgrade BERT to RoBERTa/DeBERTa for better job matching.

Add employer tools for candidate shortlisting and analytics.

Integrate knowledge graphs for skill-role mapping.

Expand interview assistant datasets for broader domain coverage.

📚 References
BERT: Devlin et al. (2018)

Gemini API: Google AI Blog

FAISS: Facebook Research
