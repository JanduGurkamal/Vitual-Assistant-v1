from get_match import in_tent
from datetime import datetime
from functools import cache, lru_cache
import os
import platform
import random
import re
import string
import sys
import time
import webbrowser
import winsound
import speech_recognition as sp
import screen_brightness_control as sbc
import requests
import pywhatkit
import pyttsx3
import pyjokes
import pyautogui
import pyperclip as pc
import psutil
from bs4 import BeautifulSoup

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 155)
OWNER_NAME = ""
lang = "en-IN"


def speak(cmdd):
    """To convert text to speech
    for interacting with user."""

    engine.say(cmdd)
    engine.runAndWait()


def get_owner_name():
    """To get device name to use it as
    name to refer to the user while interacting."""

    global OWNER_NAME
    OWNER_NAME = str(platform.node())
    name_to_use = re.split(r"[,\-;]", OWNER_NAME)
    OWNER_NAME = name_to_use[0]


def source():
    listener = sp.Recognizer()
    with sp.Microphone() as input_main:
        winsound.Beep(600, 500)
        voice = listener.listen(input_main)
    command = listener.recognize_google(voice)
    return command.lower()


def about(result, command):
    if "bye" in result.lower():
        replies = ["Bye, see you!", "Good bye!, I am always available"
            , "Bye!, nice helping you", "Ok, see you"]
        speak(random.choice(replies))
    elif "owner" in result.lower():
        speak("I was created by my owner")
    elif "language" in result.lower():
        speak("I was created in python")
    elif "name asking" in result.lower():
        speak("I am Alex")


def bot_modify(result, command):
    if "owner name" in result.lower():
        global OWNER_NAME
        speak(f"Okay {OWNER_NAME}, From now onwards, I'll call you")
        OWNER_NAME = command.split()[command.split().len]
        speak(OWNER_NAME)
    elif "language change" in result.lower():
        speak(f"OKAY, Language changed to {command.split()[0]}")


def machine_use(result, command):
    if "volume" in result.lower():
        if "volume up" in command.lower() and "play" not in command:
            commmanded_words = command.split()[-1]
            if f"{commmanded_words}".isdigit():
                for i in range(int(int(commmanded_words) / 2)):
                    pyautogui.press("volumeup")
            else:
                speak("by how much?")
                command = source()
                command = command.split()[-1]
                try:
                    for v in range(int(int(command) / 2)):
                        pyautogui.press("volumeup")
                except:
                    speak("Sorry i am not sure what you said")
        elif "volume down" in command and "play" not in command:
            commmanded_words = command.split()[-1]
            if f"{commmanded_words}".isdigit():
                for i in range(int(int(commmanded_words) / 2)):
                    pyautogui.press("volumedown")
            else:
                speak("by how much?")
                command = source()
                command = command.split()[-1]
                try:
                    for v in range(int(int(command) / 2)):
                        pyautogui.press("volumedown")
                except:
                    speak("i am not sure what you said")
    if "machine work" in result.lower():
        if "shutdown" in command:
            speak(f"Are you sure you want to shutdown the system, {OWNER_NAME}?")
            command = source()
            if "yes" in command and "no" not in command:
                speak("Shutting down the system")
                winsound.Beep(500, 1000)
                os.system("shutdown /s /t 1")
            elif "no" in command and "yes" not in command:
                speak("Ok")
            else:
                speak("Sorry could not catch it")
        elif "restart" in command:
            speak(f"Are you sure you want to restart the system, {OWNER_NAME}?")
            command = source()
            if "yes" in command and "no" not in command:
                speak("Shutting down the system")
                winsound.Beep(500, 1000)
                winsound.Beep(500, 1000)
                os.system("restart /s /t 1")
            elif "no" in command and "yes" not in command:
                speak("Ok")
            else:
                speak("Sorry could not catch it")
    elif "switch windows" in result.lower():
        pyautogui.hotkey("alt", "tab")

def tell(result, command):
        command = command.replace("what", "").replace("is", "") \
            .replace("time", "").replace("in", "").strip()
        if command in ("", " "):
            speak(f"It\'s {datetime.now().strftime('%H:%M')}")
        else:
            page = requests.get(
                f"https://www.google.com/search?q=time+in+{command.strip().lower()}&source=hp&ei"
                f"=5D5AY_y9PK_cz7sPlduVuA4&iflsig=AJiK0e8AAAAAY0BM9ZZBPDiCbT-Rr-dXkH-wfhROWS0E&ved"
                f"=0ahUKEwj8v8b9sM76AhUv7nMBHZVtBecQ4dUDCAc&uact=5&oq=time+in+london&gs_lcp"
                f"=Cgdnd3Mtd2l6EAMyCwgAEIAEELEDEIMBMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCA"
                f"BDIFCAAQgAQyBQgAEIAEOg4IABCPARDqAhCMAxDlAjoOCC4QjwEQ6gIQjAMQ5QI6EQguEIAEELEDEIMBEMcBENEDOgsILhCA"
                f"BBCxAxCDAToFCC4QgAQ6CAguEIAEELEDOggILhCxAxCDAToICAAQgAQQsQM6BwgAELEDEAo6DgguEIAEELEDEMcBENEDOgcI"
                f"ABCABBAKULwDWOMRYMsTaAFwAHgAgAG8AYgBkhKSAQQwLjE0mAEAoAEBsAEK&sclient=gws-wiz", timeout=(5, 2))

            html_to_parse = page.content
            soup = BeautifulSoup(html_to_parse, 'html.parser')
            speak("It's " + soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).string + f"in {command}")


def greet(result, command):
    if "greeting" in result.lower():
        replies = ["Hello!", "Hello!, How may I help you"
            , "Hello!, How can I help you", "Hi"]
        speak(random.choice(replies))
    elif "how are you" in result.lower():
        replies = ["I am good", "I am good, What about you", "i am fine, How are you doing today", "I am good how may I help you today"]
        speak(random.choice(replies))
    elif "bye" in result.lower():
        replies = ["Bye!, see you", "Good bye!, I am always available for you"
            , "Bye!, nice helping you", "Ok, see you"]
        speak(random.choice(replies))


def work_bot(result, command):
    if "location" in result.lower():
        speak("Let me see.")
        webbrowser.open(
            f"https://www.google.com/maps/place/"
            f"{command.replace('where', '').replace('is', '').strip()}")
        time.sleep(2.5)
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('wheresearch.png')))
        speak(f"There you go, {OWNER_NAME}")
    elif "play" in result.lower():
        command = command.replace("play", "")
        pywhatkit.playonyt(command)
    elif "calculate" in result.lower():
        command = command.replace("calculate", "").strip()
        complex_terms = ['sin', 'cos', 'tan', 'log', 'factorial', 'ceil', 'floor', 'gcd', 'lcm']
        if any(term in command for term in complex_terms):
            speak(f"Sorry {OWNER_NAME}, I am still being programmed for trigonometric or complex calculations.")
        else:
            ans = sum(map(int, re.findall(r'[+-]?\d+', command)))
            speak(f"It's {ans}")
    elif "run apps" in result.lower():
        speak("Ok")
        command = command.replace("open", "").replace("for", "").replace("me", "").strip()
        pyautogui.press('win')
        time.sleep(0.1)
        pyautogui.write(f"{command.title()}")
        time.sleep(0.1)
        pyautogui.press('enter')
    elif "search" in result.lower():
        speak("Ok, This is what I found!")
        print(pywhatkit.search(command))



def check_conditions(result, command):
    if "about" in result.lower():
        about(result, command)
    elif "greet" in result.lower():
        greet(result, command)
    elif "machine use" in result.lower():
        machine_use(result, command)
    elif "work bot" in result.lower():
        work_bot(result, command)
    elif "tell" in result.lower():
        tell(result, command)
    elif "bot modify" in result.lower():
        bot_modify(result, command)


def main():
    while True:
        try:
            command = source()
            print(command)
            result = in_tent(command)
            print(result)
            check_conditions(result, command)
            if "bye" in result.lower():
                break
        except sp.UnknownValueError:
            speak("I couldn't catch that")

main()

