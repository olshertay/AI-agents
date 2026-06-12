import ollama

def classify_intent(user_input: str) -> str:
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": "Classify the user's input into ONE category only: math, code, chat."
            },
            {"role": "user", "content": user_input}
        ]
    )

    return response["message"]["content"].strip().lower()


def math_handler(text):
    return f"[MATH AGENT] You asked: {text}"

def code_handler(text):
    return f"[CODE AGENT] You asked: {text}"

def chat_handler(text):
    return f"[CHAT AGENT] You asked: {text}"


def router(user_input: str):
    intent = classify_intent(user_input)
    print("DEBUG intent:", intent)

    if "math" in intent:
        return math_handler(user_input)
    elif "code" in intent:
        return code_handler(user_input)
    else:
        return chat_handler(user_input)


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        print(router(user_input))