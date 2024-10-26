from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st['openapi']['personal_api_key'])

def generate_response(prompt_text):
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": 'system', "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt_text}
        ],
        max_tokens=150,
        temperature=0.7
    )

    texto_retorno = response.choice[0].message.content.strip()
    return texto_retorno


if __name__ == "__main__":
    prompt_text = "Qual é a capital da França?"
    resposta = generate_response(prompt_text)
    print(resposta)