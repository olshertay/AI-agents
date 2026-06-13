import ollama

def handle(text: str) -> str:
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI SOC Operations assistant. "
                    "Help with incident response, log triage, SIEM queries, "
                    "and escalation decisions."
                )
            },
            {"role": "user", "content": text}
        ]
    )
    return f"[AI OPERATIONS]\n{response['message']['content']}"