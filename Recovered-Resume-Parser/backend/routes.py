from flask import Blueprint, request, jsonify
from backend.services.text_extraction import extract_text_from_pdf
from .services.file_upload import handle_upload
from backend.services.ai_processing import compare_jd_resume
from backend.services.scoring import rank_candidates
from backend.services.notifications import send_email
from backend.models import db, CandidateScore

routes = Blueprint("routes", __name__)

# Store job description in memory (for simplicity)
JOB_DESCRIPTION = """
We are looking for a Software Engineer with experience in Python, Flask, and AI/ML technologies.
Strong knowledge of NLP, data structures, and problem-solving skills are required.
"""

# Temporary storage for processed resumes
candidates = []

# File Upload Route**
@routes.route("/upload", methods=["POST"])
def upload_resume():
    response = handle_upload()
    if "error" in response:
        return jsonify(response), 400

    filepath = response["filepath"]
    
    # Extract text from the uploaded resume
    resume_text = extract_text_from_pdf(filepath)

    # Compare resume with job description using AI
    match_score, explanation = compare_jd_resume(JOB_DESCRIPTION, resume_text)
    
    candidate_name = "Extracted Name"  # TODO: Extract from resume_text
    candidate_email = "extracted_email@example.com"  # TODO: Extract from resume_text
    try:
        # Store result in database
        new_candidate = CandidateScore(
            name=candidate_name,
            email=candidate_email,
            match_score=match_score
        )
        db.session.add(new_candidate)
        db.session.commit()

        # # Add to temporary list
        # candidates.append({
        #     "name": "Candidate",
        #     "email": "candidate@example.com",
        #     "match_score": match_score
        # })

        return jsonify({
            "message": "Resume processed successfully!",
            "match_score": match_score,
            "explanation": explanation
        })

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Get Results Route**
@routes.route("/results", methods=["GET"])
def get_results():
    results = CandidateScore.query.order_by(CandidateScore.match_score.desc()).all()
    return jsonify([{ 
        "name": r.name, 
        "email": r.email, 
        "match_score": r.match_score, 
        "explanation": r.explanation 
    } for r in results])


# Send Email Notifications Route**
@routes.route("/notify", methods=["POST"])
def send_notifications():
    try:
        for candidate in candidates:
            if candidate["match_score"] > 70:  # Notify only if match score is high
                send_email(
                    candidate["email"],
                    "Job Application Status", 
                    f"Dear {candidate['name']},\n\nYour application scored {candidate['match_score']}! We will contact you soon."
                )

        return jsonify({"message": "Emails sent successfully!"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Health Check Route**
@routes.route("/", methods=["GET"])
def health_check():
    return jsonify({"message": "Recruitment Automation API is running!"})

# Initialize routes
def init_routes(app):
    # Register the blueprint with the app
    app.register_blueprint(routes)