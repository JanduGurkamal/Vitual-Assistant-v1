import time
import webbrowser

import psutil

from AppOpener import run

import speech_recognition as sp
import pyjokes
import pyttsx3

import re

import platform
import math

import pyaudio

import pywhatkit




def speak(cmdd):
    engine.say(cmdd)
    engine.runAndWait()


listener = sp.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 160)

owner_name = ""


def get_owner_name():
    global owner_name

    owner_name = str(platform.node())
    x = re.split(r',|-|;', owner_name)
    owner_name = x[0]


def main_function():
    global owner_name

    count = 0
    use_in_main = 0
    radian = 0
    to_check = ["sin", "tan", "cos", "log", "floor", "ceil", "lcm", "gdc", "hcf"]

    with sp.Microphone() as source:
        speak("listening....")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'tell' and 'a' and 'joke' in command:
            speak(str(pyjokes.get_joke()))

        if 'stop dumbo' or 'alexa dumbo' in command:
            pass

        if "open" in command:

            to_open = command.replace("open", '').strip()
            speak(f"Ok {owner_name}, Opening {to_open}")
            run(to_open)
            time.sleep(5)
            if "chrome.exe" in (i.name() for i in psutil.process_iter()):
                speak(f"{owner_name}, Google chrome is open")
                pass
            else:
                webbrowser.open(f"{to_open}.com")

        elif 'call me' in command:
            to_speak = f"Ok{owner_name}, From now, I will " + str(command.replace("dumbo", '').replace("me", 'you'))
            owner_name = str(command.replace("dumbo", '').replace("me", '').replace('call', '')).strip()
            print(owner_name)
            speak(to_speak)



        elif 'who are you' in command:
            speak(f"{owner_name}I am Dumbo, your virtual assistant. I was created by King")

        else:
            try:
                to_use = ""
                if 'sin' or 'cos' or 'tan' or 'log' or 'factorial' or 'ceil' or 'floor' or 'gcd' or 'lcm':

                    splitted = command.split(" ")
                    print(splitted)
                    for i in splitted:
                        count = count + 1
                        for y in to_check:
                            print(count)
                            if i == y:
                                to_use = i
                                if to_use == "sin" or to_use == "cos" or to_use == "tan":
                                    if splitted[count] == "inverse":
                                        command.replace(f"{to_use}", "").replace(f"{splitted[count]}", "").replace(f"{splitted[count+1]}")
                                        speak("I am under update regarding inverse functions")
                                    else:
                                        radian = (int(splitted[count]) * math.pi) / 180
                                        command.replace(f"{to_use}", "").replace(f"{splitted[count]}", f"{use_in_main}")
                                        print(radian)
                                        use_in_main = eval(f"math.{to_use}({radian})")
                    ans = eval(command)
                    speak(f"It's {ans}")
                    print(use_in_main)
            except Exception as f:
                print("Sorry, repeat")
                pass


try:
    get_owner_name()
    main_function()
except:
    print(
        "Wrong"
    )
    pass


"""
        elif 'who am i' or 'who i am' in command:
            speak(f"{owner_name}")
        """