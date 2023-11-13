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
import subprocess
import platform
import pyjokes
import pyautogui

image = cv2.imread("ava.jpeg")
image = cv2.resize(image, (400, 400))
cv2.imshow("AVA", image)
print('Loading your AI assistant')

engine = pyttsx3.init()
engine.setProperty('voice', engine.getProperty('voices')[1].id)
engine.setProperty('rate', 175)

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

def open_spotify():
    # Specify the command to open Spotify based on the operating system
    if platform.system() == "Darwin":  # macOS
        subprocess.run(["open", "-a", "Spotify"])
    elif platform.system() == "Windows":  # Windows
        # Provide the full path to the Spotify executable on Windows
        subprocess.run(["C:\\Users\\talk2\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe"])
    elif platform.system() == "Linux":  # Linux
        subprocess.run(["spotify"])

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
            statement=''
            return "None"
        return statement

speak("Loading your AI personal assistant")
speak("Hi, I am AVA")
wish()


if __name__=='__main__':


    while True:
        statement=''
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            pass
        elif "exit" in statement or "quit" in statement:
            image = cv2.imread("Ava2.jpeg")
            image = cv2.resize(image, (400, 400))
            cv2.destroyAllWindows()
            cv2.imshow("PowerOff", image)
            cv2.waitKey(0)
            time.sleep(2)
            cv2.destroyAllWindows()
            speak('your personal assistant G-one is shutting down,Good bye')
            print('your personal assistant G-one is shutting down,Good bye')
            exit()
        elif "good bye" in statement or "ok bye" in statement or "bye" in statement or "shut down" in statement or "stop" in statement:
            image = cv2.imread("Ava2.jpeg")
            image = cv2.resize(image, (400, 400))
            cv2.destroyAllWindows()
            cv2.imshow("PowerOff", image)
            cv2.waitKey(0)
            time.sleep(2)
            cv2.destroyAllWindows()
            speak('your personal assistant G-one is shutting down,Good bye')
            print('your personal assistant G-one is shutting down,Good bye')
            break
        elif 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'tell me a joke' in statement:
            joke = pyjokes.get_joke()
            speak(joke)
        # elif "weather" or "temperature" in statement:
        #     api_key="8ef61edcf1c576d65d836254e11ea420"
        #     base_url="https://api.openweathermap.org/data/2.5/weather?"
        #     speak("whats the city name")
        #     city_name=takeCommand()
        #     complete_url=base_url+"appid="+api_key+"&q="+city_name
        #     response = requests.get(complete_url)
        #     x=response.json()
        #     if x["cod"]!="404":
        #         y=x["main"]
        #         current_temperature = y["temp"]
        #         current_humidiy = y["humidity"]
        #         z = x["weather"]
        #         weather_description = z[0]["description"]
        #         speak(" Temperature in kelvin unit is " +
        #               str(current_temperature) +
        #               "\n humidity in percentage is " +
        #               str(current_humidiy) +
        #               "\n description  " +
        #               str(weather_description))
        #         print(" Temperature in kelvin unit = " +
        #               str(current_temperature) +
        #               "\n humidity (in percentage) = " +
        #               str(current_humidiy) +
        #               "\n description = " +
        #               str(weather_description))
        #
        #     else:
        #         speak(" City Not Found ")
        elif 'what are you' in statement:
            speak('I am Ava Generation 1 , Develop to provide assistance to Humans')
            print('I am Ava Generation 1 , Develop to provide assistance to Humans')
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print('The time is : ')
            print(strTime)
            speak(f"the time is {strTime}")
        elif 'find location' in statement:
            speak('What is the location?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            speak('Here is the location of ' + location)
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
            subprocess.run(["taskkill", "/F", "/IM", "camera_app_process_name.exe"])
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
        elif 'open' in statement:
            website = statement.replace('open', '').strip()
            if website=='spotify' in statement:
                open_spotify()
            elif website:
                url = 'https://' + website + '.com'
                webbrowser.get().open(url)
                speak(f'Opening {website}')
            else:
                speak('Please specify a website to open')
        elif 'play music' in statement:
            open_spotify()
            pyautogui.hotkey('ctrl', 'alt', 'p')
            pyautogui.press('space')
        elif 'next song' or 'next track' in statement:
            open_spotify()
            pyautogui.hotkey('ctrl','right')
        elif 'play music' in statement:
            open_spotify()
            pyautogui.hotkey('ctrl','left')
        elif "shut down" or "log off" in statement :
            image = cv2.imread("Ava2.jpeg")
            image = cv2.resize(image, (350, 350))
            cv2.imshow("PowerOff", image)
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            cv2.waitKey(0)
            subprocess.call(["shutdown", "/l"])

time.sleep(3)
