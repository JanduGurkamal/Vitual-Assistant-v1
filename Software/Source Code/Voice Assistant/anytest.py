# """from datetime import datetime
# import speech_recognition as st
# import time
# import winsound
#
# command = "set an alarm for 100"
# hr = ""
# hrs = 0
#
#
# def beat_alarm(alm):
#     time.sleep(alm)
#     for i in range(100):
#         winsound.Beep(500, 100)
#
#
# if "set alarm" in command:
#     command_list = command.split()
#     for c in command_list:
#         if c.isdigit():
#             hr = c
#             break
#     hr = int(hr)
#     u = len(str(abs(hr)))
#
#     while (u == 1 or u == 2) and "clock" not in command:
#         listener = st.Recognizer()
#         print("for what time?")
#         with st.Microphone() as source2:
#             voice2 = listener.listen(source2)
#             command2 = listener.recognize_google(voice2)
#             print(command2)
#             u = len(str(abs(int(command2))))
#             hr = int(command2)
#
#     if (u == 1 or u == 2) and "clock" not in command:
#         pass
#     elif u == 3:
#         hrs = int(hr / 100) * 3600
#     elif u == 4:
#         hrs = int(hr / 100) * 3600
#
#     min_ = int(hr % 100) * 60
#     total_seconds = hrs + min_
#
#     if int(datetime.now().strftime("%H")) > 12:
#         current_hr = (int(datetime.now().strftime("%H")) - 12) * 3600
#     else:
#         current_hr = (int(datetime.now().strftime("%H"))) * 3600
#
#     current_stm = int(datetime.now().strftime("%S"))
#     current_min = int(datetime.now().strftime("%M")) * 60
#     current_secs = current_min + current_hr + current_stm
#     if current_secs > total_seconds:
#         alarm_secs = abs((current_secs - total_seconds) + 43200)
#     else:
#         alarm_secs = abs(current_secs - total_seconds)
#     beat_alarm(alarm_secs)
# """
#
# """
# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
# import math
# # Get default audio device using PyCAW
# devices = AudioUtilities.GetSpeakers()
# interface = devices.Activate(
#     IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume = cast(interface, POINTER(IAudioEndpointVolume))
# # Get current volume
# currentVolumeDb = volume.GetMasterVolumeLevel()
# volume.SetMasterVolumeLevel(currentVolumeDb - 0.1, None)
# # NOTE: -6.0 dB = half volume !"""
#
# """import pyautogui
#
# pyautogui.press('win')
# time.sleep(0.1)llllllll
# pyautogui.write("settings")
# pyautogui.press('enter')"""
#
# """import win32gui
#
# command = "google chrome"
#
# opened_titles = pyautogui.getAllTitles()
# print(opened_titles)
# opened_hwnd = str(pyautogui.getAllWindows())
# opened_hwnd = opened_hwnd.split(",")
# print(opened_hwnd)
# matched_hwnd = ""
#
# for i, title in enumerate(opened_titles):
#     if command in title.lower():
#         matched_hwnd = str(opened_hwnd[i])
#         break
#     else:
#         pass
#
# print(matched_hwnd)"""
#
#
# """ TO OPEN OLD TO OPEN OLD TO OPEN OLD TO OPEN OLD TO OPEN OLD TO OPEN OLD TO OPEN OLD TO OPEN OLD  TO OPEN OLD
#
#             to_open = command.replace("open", '').strip()
#             speak(f"Ok {owner_name}, Opening {to_open}")
#             run(to_open)
#             time.sleep(10)
#
#             if f"{to_open}.exe" in (i.name() for i in psutil.process_iter()):
#                 speak(f"{owner_name}, {to_open} is open")
#             elif to_open == "google" or to_open == "google chrome":
#                 if "chrome.exe" in (i.name() for i in psutil.process_iter()):
#                     speak(f"{owner_name}, Google chrome is open")
#             else:
#                 webbrowser.open(f"{to_open}.com") """
#
# """ ALARM OLD ALARM OLD ALARM OLD ALARM OLD ALARM OLD ALARM OLD ALARM OLD ALARM OLD ALARM OLD ALARM OLD
#  elif "set an alarm" in command:
#             hr = ""
#             hrs = 0
#             command_list = command.split()
#             for c in command_list:
#                 if c.isdigit():
#                     hr = c
#                     break
#             hr = int(hr)
#             u = len(str(abs(hr)))
#
#             while (u == 1 or u == 2) and "clock" not in command:
#                 listener2 = sp.Recognizer()
#                 print("for what time?")
#                 with sp.Microphone() as source2:
#                     voice2 = listener2.listen(source2)
#                     command2 = listener2.recognize_google(voice2)
#                     print(command2)
#                     u = len(str(abs(int(command2))))
#                     hr = int(command2)
#
#             if (u == 1 or u == 2) and "clock" not in command:
#                 pass
#             elif u == 3:
#                 hrs = int(hr / 100) * 3600
#             elif u == 4:
#                 hrs = int(hr / 100) * 3600
#
#             min_ = int(hr % 100) * 60
#             total_seconds = hrs + min_
#
#             if int(datetime.now().strftime("%H")) > 12:
#                 current_hr = (int(datetime.now().strftime("%H")) - 12) * 3600
#             else:
#                 current_hr = (int(datetime.now().strftime("%H"))) * 3600
#
#             current_stm = int(datetime.now().strftime("%S"))
#             current_min = int(datetime.now().strftime("%M")) * 60
#             current_secs = current_min + current_hr + current_stm
#             if current_secs > total_seconds:
#                 alarm_secs = abs((current_secs - total_seconds) + 43200)
#             else:
#                 alarm_secs = abs(current_secs - total_seconds)
#
#             thread1 = Thread(target=beat_alarm, args=(alarm_secs,))
#             thread2 = Thread(target=main_function())
#             thread1.start()
#             thread2.start()"""
# """
# NMAX = 4  # declaring max power
# XMAX = 10  # declaring max number of value to work with
#
# c = 1
# # printing powers before x
# while (c <= NMAX):
#     print("%10d" % c, end="")
#     c = c + 1
#
# print()
# # printing x
# NMAX2 = NMAX  # creating copy of NMAX to not manipulate real variable value for future referance
# while (0 < NMAX2):
#     print("%10s" % "x ", end="")  # printing 'x' the number of times the set limit(NMAX)
#     NMAX2 = NMAX2 - 1
#
# print("\n", "     ", "-" * (11 * (NMAX - 1)))  # printing 1st row(heading row) seperator for clarity of content
#
# c = 0
# x = 1
# # printing table contents
# while (c < XMAX):
#     c = c + 1  # increasing value of base each time till it reaches the set limit(XMAX)
#     while (x <= NMAX):
#         print("%10.0f" % c ** x, end="")
#         x += 1  # increasing power by 1 each time till it reaches the set limit(NMAX)
#     x = 1  # resetting power value for next operations to work smoothly
#     print()
# """
# """
# file = open("languages.txt", 'r')
# file_content = file.read()
# file.close()
#
# lang = input()
# c=-1
#
# for x in file_content.split():
#     c=c+1
#     if lang.lower() in x.lower():
#         print(file_content.split()[c+1])"""
#
# """CREATING A WORD FILE OF DELIVERABLE 3"""
#
# """
#
# from docx import Document
#
# # Create a new Document
# doc = Document()
#
# # Title and Introduction
# doc.add_heading('Requirement Specification for Intelligent Virtual Assistant (IVA)', 0)
#
# doc.add_heading('Deliverable 2 - Part 1', level=1)
# doc.add_heading('1. Introduction', level=2)
# doc.add_paragraph("Purpose: This document outlines the requirements for the Intelligent Virtual Assistant (IVA) project, "
#                   "focusing on identifying functional and non-functional requirements, mapping these to scenarios, and describing those scenarios.")
# doc.add_paragraph("Scope: The IVA will understand and process natural language inputs, provide personalized responses, and handle complex queries. "
#                   "The system will be designed for scalability and ease of use.")
#
# # Current System
# doc.add_heading('2. Current System', level=2)
# doc.add_paragraph("Currently, there is no existing virtual assistant system in place. Users rely on manual processes or basic digital tools to manage their daily tasks and queries.")
#
# # Proposed System
# doc.add_heading('3. Proposed System', level=2)
#
# doc.add_heading('3.1 Overview', level=3)
# doc.add_paragraph("The proposed system is a Python-based virtual assistant that uses ML and AI to understand user inputs, provide relevant responses, and perform tasks. "
#                   "It aims to enhance user productivity and experience by offering personalized and intelligent assistance.")
#
# # Functional Requirements
# doc.add_heading('3.2 Functional Requirements', level=3)
# functional_requirements = [
#     "User Authentication: Secure user login and management.",
#     "NLP Processing: Understand and process natural language queries.",
#     "Task Management: Create, update, and delete tasks and reminders.",
#     "Information Retrieval: Provide information on various topics like weather, news, etc.",
#     "Personalization: Learn user preferences and tailor responses accordingly.",
#     "Voice Interaction: Support voice input and output.",
#     "Integration: Integrate with third-party services and APIs (e.g., calendar, email)."
# ]
# for req in functional_requirements:
#     doc.add_paragraph(req, style='List Bullet')
#
# # Nonfunctional Requirements
# doc.add_heading('3.3 Nonfunctional Requirements', level=3)
# nonfunctional_requirements = [
#     "Performance: The system should handle up to 1000 concurrent users.",
#     "Usability: The interface should be user-friendly and intuitive.",
#     "Reliability: The system should have 99.9% uptime.",
#     "Security: Ensure data privacy and protection against unauthorized access.",
#     "Scalability: The system should scale to accommodate a growing user base."
# ]
# for req in nonfunctional_requirements:
#     doc.add_paragraph(req, style='List Bullet')
#
# # System Models
# doc.add_heading('3.5 System Models', level=3)
#
# doc.add_heading('3.5.1 Scenarios', level=4)
# scenarios = [
#     "Scenario 1 (SC-1): User asks IVA for the weather forecast.",
#     "Scenario 2 (SC-2): User sets a reminder for a meeting.",
#     "Scenario 3 (SC-3): User requests IVA to send an email.",
#     "Scenario 4 (SC-4): User asks IVA for news updates.",
#     "Scenario 5 (SC-5): User manages calendar events.",
#     "Scenario 6 (SC-6): User asks for personalized recommendations."
# ]
# for scenario in scenarios:
#     doc.add_paragraph(scenario, style='List Bullet')
#
# # Matrix: Requirements - Scenarios
# doc.add_heading('Matrix: Requirements - Scenarios', level=4)
# table = doc.add_table(rows=1, cols=7)
# hdr_cells = table.rows[0].cells
# hdr_cells[0].text = 'Requirement'
# hdr_cells[1].text = 'SC-1'
# hdr_cells[2].text = 'SC-2'
# hdr_cells[3].text = 'SC-3'
# hdr_cells[4].text = 'SC-4'
# hdr_cells[5].text = 'SC-5'
# hdr_cells[6].text = 'SC-6'
#
# rows = [
#     ('REQ-1: User Authentication', '', '', 'X', 'X', 'X', 'X'),
#     ('REQ-2: NLP Processing', 'X', 'X', 'X', 'X', 'X', 'X'),
#     ('REQ-3: Task Management', '', 'X', '', '', 'X', ''),
#     ('REQ-4: Information Retrieval', 'X', '', '', 'X', '', ''),
#     ('REQ-5: Personalization', 'X', 'X', 'X', 'X', 'X', 'X'),
#     ('REQ-6: Voice Interaction', 'X', 'X', 'X', 'X', 'X', 'X'),
#     ('REQ-7: Integration', '', 'X', 'X', 'X', 'X', 'X')
# ]
#
# for row in rows:
#     cells = table.add_row().cells
#     for i, value in enumerate(row):
#         cells[i].text = value
#
# # Scenario Narratives
# doc.add_heading('Scenario Narratives', level=4)
#
# narratives = [
#     ("Scenario 1 (SC-1):", "User asks IVA for the weather forecast.",
#      "Narrative: John opens the IVA application and asks, 'What is the weather like today?' "
#      "The IVA processes the query using NLP, retrieves the weather information from an integrated weather service API, "
#      "and responds, 'Today's weather is sunny with a high of 75°F.'"),
#
#     ("Scenario 2 (SC-2):", "User sets a reminder for a meeting.",
#      "Narrative: Sarah uses the IVA to set a reminder for her meeting at 3 PM. She says, 'Set a reminder for my meeting at 3 PM.' "
#      "The IVA recognizes the task and stores it in the task management system. At 3 PM, the IVA alerts Sarah about the meeting."),
#
#     ("Scenario 3 (SC-3):", "User requests IVA to send an email.",
#      "Narrative: Alex asks the IVA, 'Send an email to Sam saying I'll be late.' The IVA processes the request, composes the email using the information provided, "
#      "and sends it through an integrated email service."),
#
#     ("Scenario 4 (SC-4):", "User asks IVA for news updates.",
#      "Narrative: Emma wants to know the latest news, so she asks, 'Give me the latest news updates.' The IVA retrieves the latest headlines from a news API and reads them out to Emma."),
#
#     ("Scenario 5 (SC-5):", "User manages calendar events.",
#      "Narrative: Mike needs to add a meeting to his calendar. He opens the IVA and says, 'Add a meeting to my calendar for tomorrow at 10 AM.' "
#      "The IVA processes this request, communicates with the calendar service API, and confirms the addition of the event."),
#
#     ("Scenario 6 (SC-6):", "User asks for personalized recommendations.",
#      "Narrative: Lily is looking for a movie to watch. She asks the IVA, 'What should I watch tonight?' The IVA analyzes her previous interactions and preferences, "
#      "retrieves relevant movie recommendations, and suggests, 'Based on your interest in action movies, you might enjoy 'Inception'.")
# ]
#
# for narrative in narratives:
#     for line in narrative:
#         doc.add_paragraph(line)
#
# # Deliverable 2 - Part 2
# doc.add_heading('Deliverable 2 - Part 2', level=1)
#
# doc.add_heading('Matrix: Scenarios – Use Cases', level=4)
# table = doc.add_table(rows=1, cols=9)
# hdr_cells = table.rows[0].cells
# hdr_cells[0].text = 'Scenario'
# hdr_cells[1].text = 'UC-1'
# hdr_cells[2].text = 'UC-2'
# hdr_cells[3].text = 'UC-3'
# hdr_cells[4].text = 'UC-4'
# hdr_cells[5].text = 'UC-5'
# hdr_cells[6].text = 'UC-6'
# hdr_cells[7].text = 'UC-7'
# hdr_cells[8].text = 'UC-8'
#
# rows = [
#     ('SC-1', 'X', '', '', '', '', '', '', ''),
#     ('SC-2', '', 'X', '', '', '', '', '', ''),
#     ('SC-3', '', '', 'X', '', '', '', '', ''),
#     ('SC-4', '', '', '', 'X', '', '', '', ''),
#     ('SC-5', '', '', '', '', 'X', '', '', ''),
#     ('SC-6', '', '', '', '', '', 'X', '', ''),
#     ('SC-7', '', '', '', '', '', '', 'X', ''),
#     ('SC-8', '', '', '', '', '', '', '', 'X')
# ]
#
# for row in rows:
#     cells = table.add_row().cells
#     for i, value in enumerate(row):
#         cells[i].text = value
#
# # Use Case Forms
# doc.add_heading('Use Case Forms', level=4)
#
# use_cases = [
#     ("Use Case #1", "Retrieve Weather Information", "Participating Actors: User, Weather Service API",
#      "Entry Condition: User requests weather information.",
#      "Flow of Events:",
#      ["User opens IVA application.", "User asks for the weather forecast.", "IVA processes the query using NLP.", "IVA retrieves weather information from the Weather Service API.",
#       "IVA presents the weather information to the user."],
#      "Exit Condition: User receives the weather forecast.", "Special Requirements: None.", "Exceptions: API service is unavailable."),
#
#     ("Use Case #2", "Set Reminder", "Participating Actors: User",
#      "Entry Condition: User requests to set a reminder.",
#      "Flow of Events:",
#      ["User opens IVA application.", "User requests to set a reminder.", "IVA processes the reminder request using NLP.", "IVA stores the reminder in the task management system.",
#       "IVA alerts the user at the specified time."],
#      "Exit Condition: Reminder is set and user is alerted.", "Special Requirements: None.", "Exceptions: System fails to store the reminder."),
#
#     ("Use Case #3", "Send Email", "Participating Actors: User, Email Service API",
#      "Entry Condition: User requests to send an email.",
#      "Flow of Events:",
#      ["User opens IVA application.", "User requests to send an email.", "IVA processes the email request using NLP.", "IVA composes the email.", "IVA sends the email using the Email Service API."],
#      "Exit Condition: Email is sent.", "Special Requirements: None.", "Exceptions: Email service is unavailable."),
#
#     ("Use Case #4", "Retrieve News Updates", "Participating Actors: User, News Service API",
#      "Entry Condition: User requests news updates.",
#      "Flow of Events:",
#      ["User opens IVA application.", "User asks for news updates.", "IVA processes the query using NLP.", "IVA retrieves news updates from the News Service API.",
#       "IVA presents the news updates to the user."],
#      "Exit Condition: User receives the news updates.", "Special Requirements: None.", "Exceptions: API service is unavailable."),
#
#     ("Use Case #5", "Manage Calendar Events", "Participating Actors: User, Calendar Service API",
#      "Entry Condition: User requests to manage calendar events.",
#      "Flow of Events:",
#      ["User opens IVA application.", "User requests to add, update, or delete a calendar event.", "IVA processes the request using NLP.",
#       "IVA interacts with the Calendar Service API to perform the requested action.", "IVA confirms the action to the user."],
#      "Exit Condition: Calendar event is managed as requested.", "Special Requirements: Integration with the user's calendar service.", "Exceptions: Calendar service is unavailable, or user authorization fails."),
#
#     ("Use Case #6", "Provide Personalized Recommendations", "Participating Actors: User",
#      "Entry Condition: User interacts with IVA regularly, allowing IVA to gather sufficient data.",
#      "Flow of Events:",
#      ["User opens IVA application.", "User asks for a recommendation or IVA proactively offers one.",
#       "IVA processes the request using NLP and analyzes user preferences using ML algorithms.", "IVA retrieves recommendations from relevant sources (e.g., streaming services, book databases).",
#       "IVA presents the personalized recommendations to the user."],
#      "Exit Condition: User receives personalized recommendations.", "Special Requirements: Data privacy and user consent for tracking preferences.", "Exceptions: Insufficient data for personalized recommendations."),
#
#     ("Use Case #7", "Real-Time Language Translation", "Participating Actors: User, Translation Service API",
#      "Entry Condition: User requests real-time translation of text or speech.",
#      "Flow of Events:",
#      ["User opens IVA application.", "User requests real-time translation.", "IVA processes the request using NLP.", "IVA sends the text to the Translation Service API.",
#       "The Translation Service API returns the translated text.", "IVA presents the translated text to the user.", "For speech translation, IVA outputs the translated speech."],
#      "Exit Condition: User receives the translated text or speech.", "Special Requirements: High accuracy and low latency translation.", "Exceptions: Translation service is unavailable or fails to translate."),
#
#     ("Use Case #8", "Health Monitoring and Assistance", "Participating Actors: User, Health Service API, Wearable Devices",
#      "Entry Condition: User interacts with IVA for health-related assistance.",
#      "Flow of Events:",
#      ["User opens IVA application.", "User requests health monitoring or assistance.", "IVA collects real-time data from connected wearable devices.",
#       "IVA processes the data and analyzes it using health monitoring algorithms.", "IVA provides real-time feedback and assistance based on the data.",
#       "IVA logs the data and provides recommendations for future activities."],
#      "Exit Condition: User receives real-time health feedback and assistance.", "Special Requirements: Integration with various health monitoring devices and compliance with health data regulations.",
#      "Exceptions: Device data unavailable or inaccurate, health service API fails to provide assistance.")
# ]
#
# for use_case in use_cases:
#     for detail in use_case:
#         if isinstance(detail, list):
#             for item in detail:
#                 doc.add_paragraph(item, style='List Bullet')
#         else:
#             doc.add_paragraph(detail)
#
# # Save the document
# doc.save('Deliverable 3 - Gurkamal Singh Jandu and Mateo Ysla.docx')
# """

import pytesseract
from PIL import Image
import requests
from io import BytesIO
import os

def is_url(path):
    return path.startswith('http://') or path.startswith('https://')

def load_image(path):
    if is_url(path):
        response = requests.get(path)
        return Image.open(BytesIO(response.content))
    else:
        return Image.open(path)

# Input can be a URL or a local file path
image_path = 'img.jpg'  # or 'path/to/your/image.jpg'

# Load the image
image = load_image(image_path)

# Perform OCR on the image
text = pytesseract.image_to_string(image)

# Print the extracted t