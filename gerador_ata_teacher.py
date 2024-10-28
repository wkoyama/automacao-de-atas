from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets['openai']['personal_api_key'])

def generate_response(prompt_system, prompt_text):

	response = client.chat.completions.create(
		model="gpt-4o-2024-08-06",  # Specify the model to use
		messages=[
			{"role": "system", "content": prompt_system},
			{"role": "user", "content": prompt_text}
		],
		max_tokens=150,			# Limits how long the response can be
		temperature=0.7			# A value between 0-1 that controls randomness
	)  # Ensure this line ends with the closing parenthesis


	texto_retorno = response.choices[0].message.content.strip()

	return texto_retorno


if __name__ == "__main__":

	prompt_text = "Qual é a capital da França."

	resposta = generate_response(prompt_text)

	print(resposta)
