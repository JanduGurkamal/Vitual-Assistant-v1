'''
Advanced Voice Assistant using python
'''

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
command = ""

def speak(cmdd):
    '''To convert text to speech
    for interacting with user.'''
    engine.say(cmdd)
    engine.runAndWait()


def get_owner_name():
    '''To get device name to use it as
    name to refer to the user while interacting.'''

    global OWNER_NAME
    global command
    OWNER_NAME = str(platform.node())
    name_to_use = re.split(r"[,\-;]", OWNER_NAME)
    OWNER_NAME = name_to_use[0]


def source():
    '''To get input from user through microphone.'''

    """global command
    listener = sp.Recognizer()
    with sp.Microphone() as input_main:
        winsound.Beep(600, 500)
        voice = listener.listen(input_main)
    command = listener.recognize_google(voice)
    return command.lower()"""

    global command
    command = input("Enter: ")
    return command.lower()


def send_to_interface():
    global command
    return command


def main_function(inpt):
    '''To initiate and run source function
    to get input from user through microphone.'''
    check_command(inpt)


def check_command(inn):
    '''To check command and responding
    as per condtions.'''
    global OWNER_NAME
    command = inn

    if "hello" in command and "what" not in command:
        replies = ["Hello!", "Hello!, How may I help you"
            , "Hello!, How can I help you", "Hi"]
        speak(random.choice(replies))

    elif "how are you" in command:
        replies = ["I am good", "I am good, what about you?"
            , "Much better", "Thanks for asking, I’m good. and you?", "Better."]
        speak(random.choice(replies))
        command = source()
        if "i am fine" in command and len(command.split()) < 4:
            speak("Nice to hear")
        else:
            check_command(command)

    elif 'tell' in command and 'a' in command and 'joke' in command:
        speak(str(pyjokes.get_joke()))

    elif "screenshot" in command or "take a screenshot" in command:
        speak("Name for the screenshot?")
        source()
        screen_shot = pyautogui.screenshot()
        screen_shot.save(f"{command}.png")

    elif "open" in command:
        speak("Ok")
        command = command.replace("open", "").replace("for", "").replace("me", "").strip()
        pyautogui.press('win')
        time.sleep(0.1)
        pyautogui.write(f"{command.title()}")
        time.sleep(0.1)
        pyautogui.press('enter')

    elif 'who am i' in command or 'who i am' in command:
        speak(f"Are you asking about yourself, {OWNER_NAME}?")

    elif 'call me' in command:
        to_speak = f"Ok{OWNER_NAME}, From now, I will " + \
                   str(command.replace("dumbo", '').replace("me", 'you'))
        OWNER_NAME = str(command.replace("dumbo", '').replace("me", '')
                         .replace('call', '')).strip()
        speak(to_speak)

    elif "stop" in command:
        winsound.Beep(1000, 100)
        winsound.Beep(500, 100)
        winsound.Beep(1000, 100)
        winsound.Beep(500, 100)
        sys.exit()

    elif "generate a random password" in command or "generate random password" in command:
        character_list = [string.ascii_letters, string.digits, string.punctuation]
        pwd = ""
        for i in range(20):
            random_char = random.choice(character_list)
            pwd = pwd + random.choice(random_char)
        pc.copy(pwd)
        speak("Ok, copied it to clipboard. paste anywhere to use.")

    elif 'who are you' in command or "what are you" in command:
        speak(f"{OWNER_NAME} I am python, your virtual assistant. I was created by King")

    elif "calculate" in command:
        command = command.replace("calculate", "").strip()
        complex_terms = ['sin', 'cos', 'tan', 'log', 'factorial'
            , 'ceil', 'floor', 'gcd', 'lcm']
        complex_present = False
        for term in complex_terms:
            if term in command:
                complex_present = True
        if complex_present:
            speak(f"Sorry {OWNER_NAME}, "
                  f"I am still being programmed for "
                  f"trigonometric or complex calculations.")
        else:
            ans = sum(map(int, re.findall(r'[+-]?\d+', command)))
            speak(f"It's {ans}")

    elif "lock" in command and (
            "this pc" in command or "this computer" in command
            or "computer" in command or "laptop" in command):
        pyautogui.hotkey('win', 'r')
        pyautogui.write('cmd')
        pyautogui.press('enter')
        pyautogui.write('Rundll32.exe user32.dll,LockWorkStation')
        pyautogui.press('enter')
        sys.exit()

    elif "where is" in command:
        speak("Let me see.")
        webbrowser.open(
            f"https://www.google.com/maps/place/"
            f"{command.replace('where', '').replace('is', '').strip()}")
        time.sleep(2.5)
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('wheresearch.png')))
        speak(f"Sorry, I am not sure where "
              f"{command.replace('where', '').replace('is', '').strip()} is.")

    elif "who is my pet" in command:
        speak("Just a little pup.")

    elif "volume up" in command and "play" not in command:
        commmanded_words = command.split()[-1]
        if f"{commmanded_words}".isdigit():
            for i in range(int(int(commmanded_words) / 2)):
                pyautogui.press("volumeup")
        else:
            speak("by how much?")
            command = source()
            command = command.split()[-1]
            for v in range(int(int(command) / 2)):
                pyautogui.press("volumeup")

    elif "volume down" in command and "play" not in command:
        commmanded_words = command.split()[-1]
        if f"{commmanded_words}".isdigit():
            for i in range(int(int(commmanded_words) / 2)):
                pyautogui.press("volumedown")
        else:
            speak("by how much?")
            command = source()
            command = command.split()[-1]
            for v in range(int(int(command) / 2)):
                pyautogui.press("volumedown")

    elif "how were you programmed" in command \
            or "which language were you programmed in" in command:
        speak("I am designed by king majorly in python "
              "and other few object oriented programming languages")

    elif "what is time" in command or "time right now" in command:
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
            speak("It's " + soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"})
                  .string + f"in {command}")

    elif "play" in command:
        command = command.replace("play", "")
        pywhatkit.playonyt(command)

    elif "battery percentage" in command:
        battery = psutil.sensors_battery()
        speak("The Battery is at" + str(battery.percent) + "%")

    elif "shutdown" in command:
        speak(f"Are you sure you want to shutdown the system, {OWNER_NAME}?")
        command = source()
        if "yes" in command and "no" not in command:
            speak("Shutting down the system")
            winsound.Beep(500, 1000)
            os.system("shutdown /s /t 1")
        elif "no" in command and "yes" not in command:
            speak("Ok")
        else:
            raise Exception

    elif "brightness" in command:
        count = 0
        if "set brightness to" in command:
            command.replace("set brightness to", "")
            command = command.split()
            for brightness_amount in command:
                if brightness_amount.isdigit():
                    count = count + 1
                    sbc.set_brightness(int(brightness_amount))
                    speak("Done")
                    break
            if count == 0:
                speak("To what level?")

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
            raise Exception

    else:
        speak("Ok, This is what I found!")
        print(pywhatkit.search(command))


def wake_up(inpp):
    '''To call the main function in loop for keeping
    assistant active.'''
    command = inpp
    while True:
        try:
            main_function(inpp)
        except sp.UnknownValueError:
            speak(
                "Sorry, I am not sure what you said."
            )
        except KeyboardInterrupt:
            winsound.Beep(400, 1000)
            sys.exit()
        except pywhatkit.core.exceptions.InternetException:
            speak("You need an Internet connection to use me")
        return command


get_owner_name()


