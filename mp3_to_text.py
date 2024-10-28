# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)

import assemblyai as aai
import streamlit as st
aai.settings.api_key = st.secrets['assemblyai']['api_key']
transcriber = aai.Transcriber()
def transcribe_text(file_name):
	
    config = aai.TranscriptionConfig( speaker_labels = True, speakers_expected = 2, language_code = 'pt' )
    transcricao = transcriber.transcribe(file_name, config = config)

    texto_transcrito = ""
    for sentenca in transcricao.utterances:
        texto_transcrito += f"Pessoa {sentenca.speaker}: {sentenca.text}"
        texto_transcrito + "\n"
    
    return texto_transcrito
    # transcript = transcriber.transcribe("./my-local-audio-file.wav")