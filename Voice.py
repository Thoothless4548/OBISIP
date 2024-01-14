import speech_recognition as sr
import pyttsx3
import os
from datetime import datetime
import webbrowser

# Initialize speech recognition
recognizer = sr.Recognizer()

# Initialize text-to-speech
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def execute_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        current_time = datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")
    elif "open" in command:
        app_name = command.split("open ")[-1]
        os.system(f"start {app_name}")
    elif "close browser" in command:
        os.system("taskkill /F /im chrome.exe")
        speak("Browsers closed successfully")
    elif "search" in command:
        query = command.split("search ")[-1]
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)
    else:
        speak("Sorry, I didn't understand that command.")

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Error connecting to Google API: {e}")
        return ""

if __name__ == "__main__":
    speak("Hello! How can I assist you today?")

    while True:
        command = listen()

        if "exit" in command:
            speak("Goodbye!")
            break

        if command:
            execute_command(command)
