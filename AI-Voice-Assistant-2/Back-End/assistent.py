# GROQ
from groq import Groq

client = Groq(api_key="API_KEY")

def ask_ai(text):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant", 
        messages=[
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content


# GEMEINI
# from google import genai

# client = genai.Client(api_key="API_KEY")

# def ask_ai(text):
#     response = client.models.generate_content(
#         model="gemini-2.0-flash",
#         contents=text
#     )
#     return response.text


# OPENAI
# from openai import OpenAI

# client = OpenAI(api_key="API_KEY")

# def ask_ai(text):
#     response = client.chat.completions.create(
#         model="gemini-2.0-flash",
#         messages=[
#             {"role": "user", "content": text}
#         ]
#     )
#     return response.choices[0].message.content







