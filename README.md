Project Title
An End-to-End AI Platform for Smart Recruitment
Integrating Job Recommendation, Resume Building, and Interview Assistance, Meeting Platform

📌 Project Overview
<img width="1361" height="695" alt="image" src="https://github.com/user-attachments/assets/6b85a770-010f-4d85-933a-1ce9de3499aa" />



This platform revolutionises traditional recruitment by leveraging AI to streamline the entire hiring lifecycle. It connects job seekers with relevant opportunities, automates resume creation, offers interview preparation, and facilitates seamless video interviews—all in one place.

<img width="1121" height="637" alt="image" src="https://github.com/user-attachments/assets/d058c826-7f71-4cd9-8be2-bcac3bb59ea0" />

<img width="1143" height="590" alt="image" src="https://github.com/user-attachments/assets/30e97339-be18-47f4-87c6-1f586b32c864" />



<img width="1141" height="636" alt="image" src="https://github.com/user-attachments/assets/3f18e254-e597-40f2-bbf7-1c61dfb3f912" />

<img width="1131" height="633" alt="image" src="https://github.com/user-attachments/assets/d70bc233-2cea-4ac1-8a22-37c257bff899" />


<img width="1120" height="607" alt="image" src="https://github.com/user-attachments/assets/8bd7e179-100d-4796-9a4a-46eddfbcc579" />




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
Python 3.8+

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
