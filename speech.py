import streamlit as st
import speech_recognition as sr

def transcribe_speech(api):
    # Initialize recognizer class
    r = sr.Recognizer()

    # Select the appropriate API
    if api == 'Google':
        recognizer_func = r.recognize_google
    elif api == 'Bing':
        recognizer_func = r.recognize_sphinx
    elif api == 'Amazon':
        recognizer_func = r.recognize_amazon
    elif api == 'Watson':
        recognizer_func = r.recognize_ibm
    else:
        return "Invalid API selected."

    # Reading Microphone as source
    with sr.Microphone() as source:
        st.info("Speak now...")
        # listen for speech and store in audio_text variable
        audio_text = r.listen(source)
        st.info("Transcribing...")

        try:
            # Use the selected API for recognition
            text = recognizer_func(audio_text)
            return text
        except:
            return "Sorry, I did not get that."

def main():
    st.title("Speech Recognition App")
    st.write("Click on the microphone to start speaking:")

    # Select the API
    api_options = ['Google', 'Bing', 'Amazon', 'Watson']
    selected_api = st.selectbox("Select API:", api_options)

    # Add a button to trigger speech recognition
    if st.button("Start Recording"):
        text = transcribe_speech(selected_api)
        st.write("Transcription: ", text)

if __name__ == "__main__":
    main()
