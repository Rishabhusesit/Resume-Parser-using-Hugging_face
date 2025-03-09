import os
from flask import request
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "backend/uploads"
ALLOWED_EXTENSIONS = {"pdf", "docx"}

def allowed_file(filename):
    return "." in filename and filename.split(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def handle_upload():
    if "file" not in request.files:
        return {"error": "No file uploaded"}, 400
    file = request.files["file"]
    if file.filename == "" or not allowed_file(file.filename):
        return {"error": "Invalid file type"}, 400
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    return {"message": "File uploaded successfully", "filepath": filepath}
