import main
import speech_recognition as so

listener2 = so.Recognizer()
while True:
    try:
        with so.Microphone() as source:
            voice3 = listener2.listen(source)
            command11 = listener2.recognize_google(voice3)
            if command11.lower() == "hey python":
                main.speak("Hi, I am python. Your virtual assistant, how may I help you?")
                main.main()
                break
    except Exception as g:
        pass
