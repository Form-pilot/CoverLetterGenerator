import requests
from fastapi import FastAPI
from fastapi import FastAPI

app = FastAPI()

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer sk-proj-cbAZADG6T7x7xHioHDNxT3BlbkFJUogsMHWzrGuhbKI8PmKx"
}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/generator")
async def generator(resume_text: str, job_description_text: str):
    # Combine the two given URLs
    data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": f"Generate a cover letter for this job posting based on the resume content provided. Don't be overly formal. Keep it somewhat brief and speak about my particular experience and how it relates to the posting. Resume text: {resume_text} Job Description text: {job_description_text}"}],
    "temperature": 0.7
}
    response = requests.post(url, json=data, headers=headers)
    return {"CoverLetter": response.json()}