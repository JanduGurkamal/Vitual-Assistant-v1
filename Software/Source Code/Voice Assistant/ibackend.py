'''
Advanced Voice Assistant using python
'''

from datetime import datetime
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
import serial
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 155)
OWNER_NAME = ""
lang = "en-IN"
command = ""

# Initialize serial communication
# ser = serial.Serial('COM3', 9600)
# time.sleep(2)  # Wait for serial communication to initialize

def speak(cmdd):
    '''To convert text to speech for interacting with user.'''
    engine.say(cmdd)
    engine.runAndWait()


def get_owner_name():
    '''To get device name to use it as name to refer to the user while interacting.'''
    global OWNER_NAME
    OWNER_NAME = str(platform.node())
    name_to_use = re.split(r"[,\-;]", OWNER_NAME)
    OWNER_NAME = name_to_use[0]


def source():
    '''To get input from user through microphone.'''
    global command
    listener = sp.Recognizer()
    with sp.Microphone() as input_main:
        winsound.Beep(600, 500)
        try:
            voice = listener.listen(input_main, timeout=5)
            command = listener.recognize_google(voice)
            return command.lower()
        except sp.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you please repeat?")
            return source()
        except sp.RequestError:
            speak("Sorry, I am unable to reach the speech recognition service.")
            return source()


def send_to_interface():
    global command
    return command


def main_function():
    '''To initiate and run source function to get input from user through microphone.'''
    global command
    command = source()
    if command:
        print(command)
        check_command()


def check_command():
    '''To check command and respond as per conditions.'''
    global OWNER_NAME
    global command


    if 'send email' in command:

        firstname = command.replace("send email to", "").strip()

        import json

        # Load the data from the JSON file
        with open('emails.json', 'r') as file:
            contacts = json.load(file)
        for contact in contacts:
            if contact['first_name'].lower() == firstname.lower():
                receiver_email = contact['email']
            else:
                speak("Could not find the email, how else can I help you!")
                return ''

        speak("What is the subject: ")
        subject = source()
        speak("What should I write in the body")
        body = source()

        # Email configuration
        sender_email = 'gurkamaljandu76@outlook.com'

        # SMTP server configuration
        smtp_server = 'smtp-mail.outlook.com'
        smtp_port = 587
        smtp_username = 'gurkamaljandu76@outlook.com'
        smtp_password = 'Gurkamal_opo1'

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the SMTP server
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(smtp_username, smtp_password)

            # Send the email
            server.send_message(msg)
            speak('Email sent successfully')

            # Disconnect from the server
            server.quit()
            main_function()
        except Exception as e:
            speak(f'Failed to send email: {e}')
            main_function()

    if "hello" in command and "what" not in command:
        replies = ["Hello!", "Hello!, How may I help you?", "Hello!, How can I help you?", "Hi"]
        speak(random.choice(replies))

    # if "turn" in command and "light" in command and "on" in command:
    #     ser.write(b'1')
    #     speak("Light turned on")
    #
    # elif "turn" in command and "light" in command and "off" in command:
    #     ser.write(b'0')
    #     speak("Light turned off")

    elif "how are you" in command:
        replies = ["I am good", "I am good. How can I help you?"]
        speak(random.choice(replies))

    elif 'tell' in command and 'a' in command and 'joke' in command:
        speak(str(pyjokes.get_joke()))

    elif "screenshot" in command or "take a screenshot" in command:
        speak("Name for the screenshot?")
        screenshot_name = source()
        screen_shot = pyautogui.screenshot()
        screen_shot.save(f"{screenshot_name}.png")
        speak("Screenshot taken")

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
        to_speak = f"Ok {OWNER_NAME}, From now on, I will call you " + \
                   str(command.replace("call me", '').strip())
        OWNER_NAME = str(command.replace("call me", '').strip())
        speak(to_speak)

    elif "stop" in command:
        winsound.Beep(1000, 100)
        winsound.Beep(500, 100)
        winsound.Beep(1000, 100)
        winsound.Beep(500, 100)
        sys.exit()

    elif "generate a random password" in command or "generate random password" in command:
        character_list = [string.ascii_letters, string.digits, string.punctuation]
        pwd = "".join([random.choice(random.choice(character_list)) for _ in range(20)])
        pc.copy(pwd)
        speak("Ok, copied it to clipboard. Paste it anywhere to use.")

    elif 'who are you' in command or "what are you" in command:
        speak(f"{OWNER_NAME}, I am Python, your virtual assistant. I was created by Gurkamal.")

    elif "calculate" in command:
        command = command.replace("calculate", "").strip()
        complex_terms = ['sin', 'cos', 'tan', 'log', 'factorial', 'ceil', 'floor', 'gcd', 'lcm']
        if any(term in command for term in complex_terms):
            speak(f"Sorry {OWNER_NAME}, I am still being programmed for trigonometric or complex calculations.")
        else:
            ans = sum(map(int, re.findall(r'[+-]?\d+', command)))
            speak(f"It's {ans}")

    elif "lock" in command and ("this pc" in command or "this computer" in command or "computer" in command or "laptop" in command):
        pyautogui.hotkey('win', 'r')
        pyautogui.write('cmd')
        pyautogui.press('enter')
        pyautogui.write('Rundll32.exe user32.dll,LockWorkStation')
        pyautogui.press('enter')
        sys.exit()

    elif "where is" in command:
        speak("Let me see.")
        location = command.replace('where is', '').strip()
        webbrowser.open(f"https://www.google.com/maps/place/{location}")
        time.sleep(2.5)
        speak(f"Here you go!")

    elif "who is my pet" in command:
        speak("Just a little pup.")

    elif "volume up" in command and "play" not in command:
        volume_value = command.split()[-1]
        if volume_value.isdigit():
            for _ in range(int(int(volume_value) / 2)):
                pyautogui.press("volumeup")
        else:
            speak("By how much?")
            volume_value = source().split()[-1]
            if volume_value.isdigit():
                for _ in range(int(int(volume_value) / 2)):
                    pyautogui.press("volumeup")
            else:
                speak("Sorry, I am not sure what you said.")

    elif "volume down" in command and "play" not in command:
        volume_value = command.split()[-1]
        if volume_value.isdigit():
            for _ in range(int(int(volume_value) / 2)):
                pyautogui.press("volumedown")
        else:
            speak("By how much?")
            volume_value = source().split()[-1]
            if volume_value.isdigit():
                for _ in range(int(int(volume_value) / 2)):
                    pyautogui.press("volumedown")
            else:
                speak("Sorry, I am not sure what you said.")

    elif "how were you programmed" in command or "which language were you programmed in" in command:
        speak("I am designed by Gurkamal, majorly in Python and a few other object-oriented programming languages.")

    elif "what is time" in command or "time right now" in command:
        command = command.replace("what", "").replace("is", "").replace("time", "").replace("in", "").strip()
        if command in ("", " "):
            speak(f"It's {datetime.now().strftime('%H:%M')}")
        else:
            page = requests.get(f"https://www.google.com/search?q=time+in+{command.strip().lower()}", timeout=(5, 2))
            soup = BeautifulSoup(page.content, 'html.parser')
            speak("It's " + soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).string + f" in {command}")

    elif "play" in command:
        command = command.replace("play", "").strip()
        pywhatkit.playonyt(command)

    elif "battery percentage" in command:
        battery = psutil.sensors_battery()
        speak("The battery is at " + str(battery.percent) + "%")

    elif "shut down" in command or "shutdown" in command:
        speak(f"Are you sure you want to shut down the system, {OWNER_NAME}?")
        if "yes" in source():
            speak("Shutting down the system")
            winsound.Beep(500, 1000)
            os.system("shutdown /s /t 1")
        else:
            speak("Ok")

    elif "brightness" in command:
        if "set brightness to" in command:
            command = command.replace("set brightness to", "").strip()
            if command.isdigit():
                sbc.set_brightness(int(command))
                speak("Done")
            else:
                speak("To what level?")

    elif "restart" in command:
        speak(f"Are you sure you want to restart the system, {OWNER_NAME}?")
        if "yes" in source():
            speak("Restarting the system")
            winsound.Beep(500, 1000)
            winsound.Beep(500, 1000)
            os.system("shutdown /r /t 1")
        else:
            speak("Ok")



def wake_up():
    '''To call the main function in loop for keeping assistant active.'''
    while True:
        try:
            main_function()
        except sp.UnknownValueError:
            speak("Sorry, I am not sure what you said.")
        except KeyboardInterrupt:
            winsound.Beep(400, 1000)
            sys.exit()
        except pywhatkit.core.exceptions.InternetException:
            speak("You need an Internet connection to use me")


# Initialize owner name at startup
get_owner_name()

# Start the wake-up loop
wake_up()
