def ai(qs):    
# Load the variables stored in .env
    load_dotenv()
# Read our secret API key
    api_key = os.getenv("GEMINI_API_KEY")
# Create a client to communicate with Gemini
    client = genai.Client(api_key=api_key)
# Send one message to Gemini
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=qs
)

# Display Gemini's answer
    print(response.text)


import os
from dotenv import load_dotenv
from google import genai

print("Welcome to the Gemini AI Chatbot!")
while True:
    print("enter 1 to continue or 0 to exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        qs=input("Enter your question: ")
        ai(qs)
    elif choice==0:
        break
    

    
    



