from openai import OpenAI
from app.core.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_llm(question, context):
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a maintenance assistant."},
            {"role": "user", "content": f"Context:\n{context}\n\nQ: {question}"}
        ]
    )
    return res.choices[0].message.content
