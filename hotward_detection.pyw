import speech_recognition as sr
import os


def take_command(print_command=True):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if print_command:
            print("Listening...")
        audio = r.listen(source)
        try:
            if print_command:
                print("Recognizing...")
            q = r.recognize_google(audio, language='en-IN')
            if print_command:
                print(f"User said: {q}\n")
        except Exception:
            # speak("I can't understand you sir")
            return "None"
        return q.lower()


while True:
    wake_up = take_command()
    if 'wake up' in wake_up:
        os.startfile('jarvis.py')
