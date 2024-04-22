import pyttsx3

engine = pyttsx3.init()

def speak(dialogue):
    engine.say(dialogue)
    engine.runAndWait()
