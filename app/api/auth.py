from fastapi import FastAPI
from app.api import auth, documents, chat

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(documents.router, prefix="/documents")
app.include_router(chat.router, prefix="/chat")
