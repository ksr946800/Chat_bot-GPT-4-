import openai

# Initialize the OpenAI client with the API key directly
client = openai.OpenAI(api_key="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")

def chat_bot1(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("ChatBot initialized. Type 'quit', 'exit', or 'bye' to stop.")
    while True:
        user_ip = input("User: ")
        if user_ip.lower() in ["quit", "exit", "bye"]:
            print("Bot: Goodbye!")
            break
        response = chat_bot1(user_ip)
        print("Bot:", response)
