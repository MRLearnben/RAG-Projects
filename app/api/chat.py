from fastapi import APIRouter
from app.services.rag import ask_llm
from app.api.documents import docs

router = APIRouter()

@router.post("/")
def chat(question: str):
    context = "\n".join(docs[-3:]) if docs else "No docs"
    answer = ask_llm(question, context)
    return {"answer": answer}
