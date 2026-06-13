import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "Say hello and explain what an AI agent is."}
    ]
)

print(response["message"]["content"])

"""
Make sure main.py actually calls the router
from router.root_router import route_input

def main():
    while True:
        user_input = input("Input: ")

        result = route_input(user_input)
        print(result)

if __name__ == "__main__":
    main()

"""