import ollama

def handle(text: str) -> str:
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI Threat Intelligence analyst. "
                    "Identify IOCs, TTPs, threat actors, and MITRE ATT&CK techniques. "
                    "Be specific and structured."
                )
            },
            {"role": "user", "content": text}
        ]
    )
    return f"[AI THREAT]\n{response['message']['content']}"