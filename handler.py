def math_handler(text):
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": "You are a math tutor. Solve clearly and show steps."},
            {"role": "user", "content": text}
        ]
    )
    return response["message"]["content"]

def code_handler(text):
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": "You are a senior software engineer. Write clean, commented code."},
            {"role": "user", "content": text}
        ]
    )
    return response["message"]["content"]