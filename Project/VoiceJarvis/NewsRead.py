import requests
import json
import pyttsx3

engine=pyttsx3.init('sapi5')
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestNews():
    api_dict={"business":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=2f10cae1151c44feb65900f3ba577517",
             "health": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=2f10cae1151c44feb65900f3ba577517",
             "technology": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=2f10cae1151c44feb65900f3ba577517",
             "sports": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=2f10cae1151c44feb65900f3ba577517",
             "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=2f10cae1151c44feb65900f3ba577517",
             "science": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=2f10cae1151c44feb65900f3ba577517",
    }

    content=None
    url=None
    speak("which field news do you want,[business],[health],[technology],[sports],[entertainment],[science]")
    field=input("type the field news that you want: ")
    for key,value in api_dict.items():
        if key.lower() in field.lower():
            url=value
            print(url)
            print("url was found")
        else:
            url=True
    if url is True:
        print("Url not found")

    news=requests.get(url).text
    news=json.loads(news)
    speak("Here is the first news")

    arts=news["articles"]
    for articles in arts:
        article=articles["title"]
        print(article)
        speak(article)
        news_url=articles["url"]
        print(f"for more info visit {news_url}")

        speak("thats all")
        a=input("Press 1  to continue and press 2 to stop")
        if str(a) =="1":
            pass
        if str(a)=="2":
            break


