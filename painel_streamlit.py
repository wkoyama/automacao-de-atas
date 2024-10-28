from moviepy.editor import *
from mp4_to_mp3 import *
from mp3_to_text import *
from gerador_ata_teacher import *

import streamlit as st

import uuid

# def mp4_to_mp3(mp4_filename, mp3_filename):
#     arquivo_a_ser_convertido = AudioFileClip(mp4_filename)
#     arquivo_a_ser_convertido.write_audiofile(mp3_filename)
#     arquivo_a_ser_convertido.close()

st.title('Automacao de atas')
st.write('Criando uma ferramenta de automação de atas de reunião com tecnologia de IA com python')

uploaded_file = st.file_uploader("Selecione o seu arquivo", accept_multiple_files=False, type = ['.mp4'])

if uploaded_file: 
    mp3_filename = ''
    with st.spinner('Convertendo de mp4 para mp3'):
        mp4_filename = uploaded_file.name
        mp3_filename = '{nome_arquivo}.mp3'.format(nome_arquivo = uuid.uuid4().hex)
        
        temp_file = open(mp4_filename, 'wb')
        temp_file.write(uploaded_file.read())

        mp4_to_mp3(mp4_filename, mp3_filename)

        st.success('Conversão de MP4 para MP3 realizada!')

    texto_transcrito = ''
    with st.spinner('Convertendo de mp3 para texto'): 
        texto_transcrito = transcribe_text(mp3_filename)

    st.success('Transcrição de MP3 realizada!')

    with st.spinner('Gerando ata de reunião'):
        prompt_system = 'Você é um ótimo gerente de projetos com grandes capacidades de criação de atas de reunião'
        prompt_text =  'Em uma redação de nível especializado, resuma as notas da reunião em um único parágrafo. Em seguida, escreva uma lista de cada um de seus pontos-chaves tratados na reunião. Por fim, liste as próximas etapas ou itens de ação sugeridos pelos palestrantes, se houver.'
        prompt_text += '==========='
        prompt_text += texto_transcrito

        texto_retorno = generate_response(prompt_system, prompt_text)

        st.markdown('Ata', texto_retorno)
        st.text_area('Transcrição',texto_transcrito)
    
    st.success("Transcrição realizada!")
