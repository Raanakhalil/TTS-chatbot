import streamlit as st
from gtts import gTTS

def text_to_speech(text, lang):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("output.mp3")
    return "output.mp3"

st.title("Text to Speech Chatbot")

user_input = st.text_input("آپ کیا کہنا چاہتے ہیں؟")
language = st.selectbox("کون سی زبان؟", ["urdu", "english"])

if st.button("آواز میں تبدیل کریں"):
    lang_code = 'ur' if language.lower() == 'urdu' else 'en'
    audio_file = text_to_speech(user_input, lang_code)
    st.audio(audio_file, format='audio/mp3')

