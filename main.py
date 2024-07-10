import requests
from conf import API_KEY 


# URL эндпоинта
URL = "https://api.proxyapi.ru/openai/v1/chat/completions"


def send_message(message):
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"}
    data = {"model": "gpt-4-turbo", "messages": [{"role": "user", "content": message}]}
    response = requests.post(URL, headers=headers, json=data)
    return response.json()


# Приветствие
print("Welcome to the chat! Type 'exit' to quit.")

# Основной цикл чата
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    bot_response = send_message(user_input)
    bot_reply = bot_response["choices"][0]["message"][
        "content"
    ]  # Извлекаем текст ответа из JSON
    print("Bot:", bot_reply)
