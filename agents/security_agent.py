import ollama

def handle(text: str) -> str:
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI Security analyst. "
                    "Analyze vulnerabilities, CVEs, misconfigurations, "
                    "and security posture. Be precise and technical."
                )
            },
            {"role": "user", "content": text}
        ]
    )
    return f"[AI SECURITY]\n{response['message']['content']}"