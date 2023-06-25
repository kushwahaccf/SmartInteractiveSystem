import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import speech_recognition as sr
import webbrowser
import requests
from bs4 import BeautifulSoup
import datetime
import random

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        r.energy_threshold=300
        audio=r.listen(source,0,4)

    try:
        print("understanding....")
        query=r.recognize_google(audio,language='en-in')
        print(f"you said:{query}")
    except Exception as e:
        print("Say that again")
        return "None"

    return query

query = takecommand().lower()

engine=pyttsx3.init('sapi5')
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
print(voices[0])


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wikipediasearch(query):
    if 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

def searchYoutube(query):
    if "youtube" in query:
        speak("That is what i found for your search")
        query=query.replace("youtube search","")
        query=query.replace("youtube","")
        query=query.replace("jarvis","")
        web="https://www.youtube.com/results?search_query="+query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done Sir")

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query=query.replace("jarvis","")
        query=query.replace("search","")
        query=query.replace("in","")
        query=query.replace("google search","")
        query=query.replace("google","")
        speak("This is what i found on google")

        try:
            pywhatkit.search(query)
            result=googleScrap.summary(query,1)
            speak(result)

        except:
            speak("no Speakabke output available")

def temperature(query):
    search="temperature in kashipur"
    url=f"https://www.google.com/search?q={search}"
    r=requests.get(url)
    data=BeautifulSoup(r.text,"html.parser")
    temp=data.find("div", class_="BNeawe").text
    speak(f"current{search} is {temp}")

def getTime():
    strTime=datetime.datetime.now().strftime("%H:%M")
    speak(f"sir the time is {strTime}")


def favMusic():
    speak("playing your favorite songs")
    a = [1, 2, 3]
    b = random.choice(a)
    if b == 1:
        webbrowser.open("https://www.youtube.com/watch?v=RbwpXJvC4yc")
    elif b==2:
        webbrowser.open("https://www.youtube.com/watch?v=DKNpHQaqRrY")
    else:
        webbrowser.open("https://www.youtube.com/watch?v=9M0jQcRoQEQ")


