import ollama


def generate_answer(question, context):

    prompt = f"""
You are a document assistant.

Answer ONLY using the provided context.

If the answer is not found in the context, say:
"I could not find this information in the document."

Context:
{context}

Question:
{question}
"""

    response = ollama.chat(
        model="phi3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]