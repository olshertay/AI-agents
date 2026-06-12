import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "Say hello and explain what an AI agent is."}
    ]
)

print(response["message"]["content"])