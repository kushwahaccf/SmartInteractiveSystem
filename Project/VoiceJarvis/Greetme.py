import pyttsx3
import datetime

engine=pyttsx3.init('sapi5')
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
print(voices[0])


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good Morning Sir")
    elif hour>12 and hour<=18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")

    speak("Please Tell me how can i help you")

