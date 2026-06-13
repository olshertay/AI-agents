import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "Say hello and explain what an AI agent is."}
    ]
)

print(response["message"]["content"])

from root_router import router

def main():
    print("=== BTREE Security AI ===")
    while True:
        user_input = input("\nYou: ").strip()
        if not user_input:
            continue
        result = router(user_input)
        print(result)

if __name__ == "__main__":
    main()