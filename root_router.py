import ollama

def classify_intent(user_input: str) -> str:
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": (
                    "Classify the user's input into ONE category only: "
                    "security, threat, operations. "
                    "Respond with a single word."
                )
            },
            {"role": "user", "content": user_input}
        ]
    )
    return response["message"]["content"].strip().lower()


def router(user_input: str) -> str:
    intent = classify_intent(user_input)
    print(f"[ROUTER] Classified as: {intent}")

    if "security" in intent:
        from agents.security_agent import handle as security_handle
        return security_handle(user_input)
    elif "threat" in intent:
        from agents.threat_agent import handle as threat_handle
        return threat_handle(user_input)
    elif "operations" in intent:
        from agents.ops_agent import handle as ops_handle
        return ops_handle(user_input)
    else:
        return "[ROUTER] Could not classify input. Please rephrase."


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        print(router(user_input))