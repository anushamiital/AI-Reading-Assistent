# AI-Reading-Assistent
**Project Title:** AI-Powered Assistive Reading Prototype for Dyslexic Learners

**Student Name:** Anusha Mittal

**Enrollment NO.** : 22118012



## **📘 Project Overview**

This project is a prototype of an AI-driven assistive reading tool designed to support learners with dyslexia. It demonstrates how speech recognition, basic attention monitoring, and personalized feedback can work together to improve reading accuracy and engagement.



The system asks the learner to read a displayed sentence aloud, uploads the audio, and uses automatic speech recognition (ASR) to transcribe it. The prototype then highlights incorrectly spoken or skipped words and provides gentle corrective feedback through an AI mentor. A simple webcam check is included to show whether the learner is present and focused, representing the attention-monitoring component of the full system.



### 📂 Folder Contents

* **app.py** — Streamlit web application for running the prototype



* **sample\_audios**/ — Example audio files used for testing (correct.wav, wrong.wav)



* **Prototype video** - demo video showing the app (video link https://drive.google.com/file/d/1PaX8denaFzWyw-HJnVbSqHFqptZVfHTa/view?usp=drive_web)



* **README.txt** — This file



### ▶️ How to Run the Prototype

##### 1\. Set up environment

Install Python 3.9+

(Optional but recommended) Create and activate a virtual environment.



##### 2\. Install dependencies

pip install streamlit SpeechRecognition pydub

conda install -c conda-forge ffmpeg   # required for audio conversion

##### 

##### 3\. Run the application

streamlit run app.py

##### 

##### 4\. Using the application

* Select a sentence from the dropdown.



* Record yourself reading the sentence and upload the audio file (wav/mp3).



* The system transcribes your speech and highlights any mismatched words.



* Allow or deny camera access — the system marks attention status accordingly.



* Read the generated mentor feedback.



#### 🎯 Purpose of the Prototype

This prototype demonstrates the key ideas of an AI reading assistant:



* Real-time speech feedback



* Identification of misread words



* Simple attention awareness



* Supportive and adaptive learning through AI-generated hints



The prototype does not aim to be a full product but rather a proof-of-concept showing how AI can improve reading support for dyslexic learners.




