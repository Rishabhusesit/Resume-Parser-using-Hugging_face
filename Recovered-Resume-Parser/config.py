import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://rishabhtiwari@host.docker.internal:5432/recruitment_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

