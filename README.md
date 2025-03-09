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

