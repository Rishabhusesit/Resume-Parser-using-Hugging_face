import re
from openai import OpenAI
from backend.config import Config
from backend.models import db, CandidateScore

# Initialize OpenAI client
client = OpenAI(api_key=Config.OPENAI_API_KEY)

def compare_jd_resume(job_description, resume_text):
    """
    Compare a job description with a resume and provide a match score and explanation.
    """
    prompt = f"""
    Job Description:
    {job_description}

    Candidate Resume:
    {resume_text}

    Analyze the resume and provide a match score out of 100 based on how well it aligns with the job description.
    Also, provide a detailed explanation for the score.

    Format:
    Match Score: <score>/100
    Explanation: <detailed explanation>
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        response_text = response.choices[0].message.content.strip()

        # Extract match score safely
        match_score = 0.0
        match = re.search(r'Match Score:\s*(\d+)', response_text)
        if match:
            match_score = float(match.group(1))

        print(f"Extracted Match Score: {match_score}")
        print(f"Explanation: {response_text}")

        return match_score, response_text

    except Exception as e:
        print(f"Error: {e}")
        return 0.0, "Error processing request."


def process_candidate_data(candidate_data):
    try:
        match_score = candidate_data.get('match_score')

        # Ensure match_score is a float
        if isinstance(match_score, (tuple, list)):  
            match_score = float(match_score[0])  
        elif isinstance(match_score, str):  
            match_score = float(re.search(r"\d+", match_score).group()) if re.search(r"\d+", match_score) else 0.0

        print(f"Final Match Score: {match_score}")

        # Insert data using SQLAlchemy ORM
        new_candidate = CandidateScore(
            name=candidate_data.get('name'),
            email=candidate_data.get('email'),
            match_score=match_score
        )
        db.session.add(new_candidate)
        db.session.commit()

    except Exception as e:
        print(f"Error: {e}")
        db.session.rollback()
