# Resume-Parser-using-Hugging_face

This project automates the recruitment process by analyzing resumes and matching them with job descriptions using AI. It extracts text from resumes, compares them with job descriptions, scores candidates, and stores results in a PostgreSQL database.

Features

Resume Parsing: Extracts text from PDFs using PyMuPDF.
AI-Powered Matching: Uses OpenAI models and Hugging Face's Sentence Transformers to compare resumes with job descriptions.
Candidate Ranking: Scores candidates based on job relevance.
Database Storage: Stores candidate details in PostgreSQL using SQLAlchemy.
Email Notifications: Sends automated emails to high-scoring candidates.
API Endpoints: Built with Flask for easy integration.

Libraries Used

Hugging Face: sentence-transformers
OpenAI: openai
SpaCy: spacy
Flask: flask, flask-cors, flask-sqlalchemy, flask-migrate
PostgreSQL: psycopg2-binary
Others: PyMuPDF, pandas, httpx

Installation

1️ Clone the Repository

git clone https://github.com/Rishabhusesit/Resume-Parser-using-Hugging_face.git
cd Resume-Parser-using-Hugging_face

2️ Create a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  

3️ Install Dependencies

pip install -r requirements.txt

4️ Set Up PostgreSQL Database

sudo apt update && sudo apt install postgresql postgresql-contrib
psql

Run the following commands in PostgreSQL shell:

CREATE DATABASE recruitment_db;
CREATE USER recruiter_user WITH ENCRYPTED PASSWORD 'securepassword';
GRANT ALL PRIVILEGES ON DATABASE recruitment_db TO recruiter_user;

Exit the shell with \q.

5 Start the Server

python app.py

