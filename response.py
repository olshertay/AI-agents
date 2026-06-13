from response import build_response

def router(user_input: str):
    intent = classify_intent(user_input)
    if "math" in intent:
        result = math_handler(user_input)
    elif "code" in intent:
        result = code_handler(user_input)
    else:
        result = chat_handler(user_input)
    return build_response(result)