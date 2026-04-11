import os
from groq import Groq
# Assuming your config file only needs the GROQ_API_KEY now
from app.core.config import GROQ_API_KEY 

# Initialize Groq client for high-speed industrial inference
client = Groq(api_key=GROQ_API_KEY)

def ask_llm(question, context):
    """
    Direct Groq implementation using Llama 3.1 70B.
    Optimized for sub-second maintenance troubleshooting.
    """
    
    # System prompt ensures the AI stays focused on technical manuals
    system_message = (
        "You are an expert Industrial Maintenance Assistant. "
        "Provide clear, step-by-step troubleshooting instructions based "
        "strictly on the provided manual context. If the answer isn't in "
        "the context, state that clearly."
    )
    
    user_message = f"TECHNICAL CONTEXT:\n{context}\n\nUSER QUERY: {question}"

    try:
        response = client.chat.completions.create(
            # llama-3.1-70b provides the best balance of logic and speed
            model="llama-3.1-70b-versatile",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            temperature=0,      # Zero creativity for technical safety
            max_tokens=1024,    # Sufficient for detailed maintenance steps
            top_p=1,
            stream=False        # Set to True if you want 'typewriter' effect in UI
        )
        
        return response.choices[0].message.content

    except Exception as e:
        return f"Industrial API Error: {str(e)}"

# Example usage for your demo:
# answer = ask_llm("How to reset the E102 error?", "Manual segment: Press red button for 5s...")
