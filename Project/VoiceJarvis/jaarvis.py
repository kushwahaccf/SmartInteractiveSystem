import pyttsx3
import speech_recognition as sr
from Project.VoiceJarvis.Greetme import greetMe
from Project.VoiceJarvis.SearchNow import searchYoutube,wikipediasearch,searchGoogle,temperature,getTime
from Project.VoiceJarvis.DictApp import openMethodTwo,closeappweb
import os
import pyautogui
from Project.VoiceJarvis.Keyboard import volumeDown,volumeUp,switch
from Project.VoiceJarvis.SearchNow import favMusic
from Project.VoiceJarvis.NewsRead import latestNews
import speedtest

class VoiceJarvis():

    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        self.voices =self.engine.getProperty("voices")
        self.engine.setProperty("voice", self.voices[1].id)

    def speak(self,audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def alarm(query):
        timehere = open("Alarmtext.txt", "a")
        timehere.write(query)
        timehere.close()
        os.startfile("alarm.py")

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.....")
            r.pause_threshold = 1
            r.energy_threshold = 300
            audio = r.listen(source, 0, 4)

        try:
            print("understanding....")
            query = r.recognize_google(audio, language='en-in')
            print(f"you said:{query}")
        except Exception as e:
            print("Say that again")
            return "None"

        return query

    def runJarvis(self):
        while True:
            query = self.takecommand().lower()
            if "wake up" in query:
                greetMe()

                while True:
                    query = self.takecommand().lower()
                    if "go to sleep" in query:
                        self.speak("Ok sir, You can call me anytime")
                        break

                    elif "wake up" in query:
                        self.speak("I am here Sir")


                    elif "open" in query:
                        # openappweb(query)
                        openMethodTwo(query)

                    elif "close" in query:
                        closeappweb(query)


                    elif "youtube" in query:
                        searchYoutube(query)

                    elif "wikipedia" in query:
                        wikipediasearch(query)

                    elif "google" in query:
                        searchGoogle(query)

                    elif "set an alarm" in query:
                        print("input time example:-  10 and 10 and 10")
                        self.speak("Set the alarm")
                        a = input("Please Tell the Time :- ")
                        self.alarm(a)
                        self.speak("done sir")

                    elif "pause" in query:
                        pyautogui.press("k")
                        self.speak("Video paused")

                    elif "play" in query:
                        pyautogui.press("k")
                        self.speak("videos played")

                    elif "mute" in query or "unmute" in query:
                        pyautogui.press("m")

                    elif "volume up" in query:
                        self.speak("tu rning volume up")
                        volumeUp()

                    elif "volume down" in query:
                        self.speak("turning volume down")
                        volumeDown()

                    elif "temperature" in query:
                        temperature(query)

                    elif "time" in query:
                        getTime()

                    elif "tired" in query:
                        favMusic()

                    elif "internet speed" in query:
                        wifi = speedtest.Speedtest()
                        upload_net = int(wifi.upload() / 1048576)
                        download_net = int(wifi.download() / 1048576)
                        print("wifi download speed is", download_net)
                        print("wifi upload speed is", upload_net)
                        self.speak(f"wifi download speed is {download_net} MB per second")
                        self.speak(f"wifi upload speed is {upload_net} MB per second")


                    elif "news" in query:
                        latestNews()

                    elif "switch" in query:
                        switch()

                    elif "change tab" in query:
                        pyautogui.hotkey("ctrl", "tab")


                    elif "told you to remember" in query:
                        remember = open("Remember.txt", "r")
                        self.speak("You told me to " + remember.read())

                    elif "please remember" in query:
                        rememberMessage = query.replace("remember that", "")
                        rememberMessage = query.replace("jarvis", "")
                        self.speak("you told me to remember that" + rememberMessage)
                        remember = open("Remember.txt", "w")
                        remember.write(rememberMessage)
                        remember.close()


                    elif "terminate yourself" in query:
                        self.speak("Okay sir")
                        exit()

                    elif "shutdown system" in query:
                        self.speak("Are you sure you want to shutdown")
                        shutdown = input("Do you wish to shutdown your computer?{yes/no}")
                        if shutdown == "yes":
                            os.system("shutdown /s /t 1")
                        elif shutdown == "no":
                            print("okay continue")

# VoiceJarvis=VoiceJarvis()
# VoiceJarvis.runJarvis()