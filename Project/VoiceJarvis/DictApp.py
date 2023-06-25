import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine=pyttsx3.init('sapi5')
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp={"commandprompt":"cmd","paint":"paint","word":"winword",
         "excel":"excel","chrome":"chrome","code":"vscode","powerpoint":"powerpnt"}

def openappweb(query):
    speak("launching , sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query=query.replace("open","")
        query=query.replace("jarvis","")
        query=query.replace("launch","")
        query=query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys=list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")

def openMethodTwo(query):
    query=query.replace("open","")
    pyautogui.press("super")
    pyautogui.typewrite(query)
    pyautogui.sleep(2)
    pyautogui.press("enter")




def closeappweb(query):
    speak("closing sir")
    if "tab" in query or "tap" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
    elif "active app" in query:
        pyautogui.hotkey("alt", "f4")
        sleep(0.5)
    else:
        keys=list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")

    speak("done sir")






