from fastapi import FastAPI
from backend.routes.law_routes import router as law_router

app = FastAPI(title="Legal Chatbot API")

app.include_router(law_router, prefix="/api")

@app.get("/")
def home():
    return {"message": "Legal Chatbot API is running!"}
