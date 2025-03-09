FROM python:3.9
WORKDIR /app
COPY requirements.txt requirements.txt
# COPY backend/app.py app.py
COPY backend/ /app/
COPY frontend/ /app/

RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
RUN pip install --upgrade openai httpx
