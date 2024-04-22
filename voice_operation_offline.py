from vosk import Model, KaldiRecognizer
import pyaudio
import os

import mainfile

# VOSK Model Lite
model = Model(r"C:\\Users\\HP\Desktop\\New Codings\\Btech main Project\\vosk-model-small-en-in-0.4")

# VOSK Model Large
# model = Model(r"C:\\Users\\HP\Desktop\\New Codings\\Btech main Project\\vosk-model-en-in-0.5")

recognizer = KaldiRecognizer(model, 16000) 

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192) 
stream.start_stream()

def start_listening():
    data = stream.read(4096)
    
    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        print(f"{text[14:-3]} ")

        if "stop listening" in text:
            quit()

        if "identify" in text:
            mainfile.speak("Opening Identifier")
            os.startfile("C:\\Users\\HP\\Desktop\\New Codings\\btech main project\\recognizer_attempt1.py")

        if "add" in text:
            mainfile.speak("Opening Face data collection script")
            os.startfile("C:\\Users\\HP\\Desktop\\New Codings\\btech main project\\face_data_collection_attempt_1.py")

while True:
    start_listening()