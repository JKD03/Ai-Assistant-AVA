import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import sys
import cv2

image = cv2.imread("C:\\Users\\talk2\\OneDrive\\Desktop\\PROGRAMMING\\AI-Personal-Voice-assistant-using-Python-master\\ava.jpeg")
image = cv2.resize(image, (400, 400))
cv2.imshow("AVA", image)

print('Loading your AI assistant')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('rate', 175)
engine.setProperty('volume', 5.7)
engine.setProperty('voice',voices[1].id)
# engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
# voiceFemales = filter(lambda v: v.gender == 'VoiceGenderFemale', voices)
# for v in voiceFemales:
#     engine.setProperty('voice', v.id)
#     engine.say('Hello world from ' + v.name)
#     engine.runAndWait()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning")
        print("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        print("Good Afternoon")
    else:
        speak("Good Evening")
        print("Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading your AI personal assistant")
speak("Hi, I am AVA")
wish()


if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "bye" in statement or "shut down" in statement or "stop" in statement:
            image = cv2.imread("C:\\Users\\talk2\\OneDrive\\Desktop\\PROGRAMMING\\AI-Personal-Voice-assistant-using-Python-master\\Ava2.jpeg")
            image = cv2.resize(image, (400, 400))
            cv2.destroyAllWindows()
            cv2.imshow("PowerOff", image)
            cv2.waitKey(0)
            time.sleep(2)
            cv2.destroyAllWindows()
            speak('your personal assistant G-one is shutting down,Good bye')
            print('your personal assistant G-one is shutting down,Good bye')
            break



        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" or "temperature"in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")

        elif 'what are you' in statement:
            speak('I am Ava Generation 1 , Develop to provide assistance to Humans')
            print('I am Ava Generation 1 , Develop to provide assistance to Humans')

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print('The time is : ')
            print(strTime)
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('Hello, I am Ava, your personal assistant. My programming enables me to assist you with various tasks such as'
                  'opening YouTube, Google Chrome, Gmail, and Stack Overflow. I can also predict the time, capture photos, search Wikipedia, provide' 
                  'weather forecasts for different cities, and fetch the latest headlines from Times of India.'
                  'Additionally, I can assist you with computational or geographical questions. Feel free to ask me anything or request my help with any of these tasks.')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Jaskarandeep")
            print("I was built by Jaskarandeep")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)


        elif "log off" in statement or "sign out" in statement:
            image = cv2.imread("C:\\Users\\talk2\\OneDrive\\Desktop\\PROGRAMMING\\AI-Personal-Voice-assistant-using-Python-master\\Ava2.jpeg")
            image = cv2.resize(image, (350, 350))
            cv2.imshow("PowerOff", image)
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            cv2.waitKey(0)
            subprocess.call(["shutdown", "/l"])

time.sleep(3)












