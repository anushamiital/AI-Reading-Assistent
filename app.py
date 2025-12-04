import streamlit as st 
import speech_recognition as sr
from pydub import AudioSegment
import difflib
import tempfile
import io

st.set_page_config(layout="centered")
st.title("Athena-Mini Assistive Reading Demo")

SENTENCES = [
    "The three thin thieves thought about the thick thorn.",
    "She sells seashells by the seashore.",
    "He threw three stones through the window."
]
sentence = st.selectbox("Choose a sentence", SENTENCE)
st.markdown(f"### Read aloud: **{sentence}**")

st.write("Step 1 - Record on your phone and upload the audio file (mp3/wav).")
uploaded = st.file_uploader("Upload audio", type = ["wav","mp3","m4a","ogg"])

cam = st.camera_input("Step 2 - (Optional) Allow the camera briefly to show focused/distracted status")

if cam is not None:
    st.success("Camera ")
