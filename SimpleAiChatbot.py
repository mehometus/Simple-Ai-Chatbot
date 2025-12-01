from groq import Groq



client = Groq(api_key="YOUR_API_KEY_HERE") # replace with your Groq API key

print("Ai Chatbot Ready!")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        print("Exiting Ai Chatbot. Goodbye!")
        break

    response = client.chat.completions.create(
        # you might need to change the model name if groq doesnt support it anymore or you have access to a different one
        model="llama-3.1-8b-instant", 
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )
 
    reply = response.choices[0].message.content
    print("\nGroq Chatbot:", reply)

