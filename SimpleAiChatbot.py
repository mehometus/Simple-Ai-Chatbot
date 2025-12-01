from groq import Groq



client = Groq(api_key="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")

print("Ai Chatbot Ready!")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        print("Exiting Ai Chatbot. Goodbye!")
        break

    response = client.chat.completions.create(
        # CHANGE THIS LINE: Use a current model name, like llama3-8b-8192
        model="llama-3.1-8b-instant", 
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )
 
    reply = response.choices[0].message.content
    print("\nGroq Chatbot:", reply)

