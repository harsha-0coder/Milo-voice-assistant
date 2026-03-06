import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
from googlesearch import search
import webbrowser
from pytube import YouTube
import os
import pywhatkit

# Initialize the text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(audio):
    """Speak the given text."""
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """Greet the user based on the current time."""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning")
    elif 12 <= hour < 16:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am Milo, please tell me how I can help you.")

def introduction():
    """Introduce Milo."""
    intro_message = "Namaste. I am Milo, created by Harsh Rajni Chourasia on 19 April 2024."
    print(intro_message)
    speak(intro_message)

def take_command():
    """Listen to the user's command and return it as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting to ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from the speech recognition service; {e}")
        return None

def execute_command(command):
    """Execute the user's command."""
    if "introduce yourself" in command:
        introduction()
    elif "wikipedia" in command:
        search_wikipedia(command)
    elif "search google" in command or "google" in command:
        google_search()
    elif "play music" in command:
        speak("Which song do you want to listen to?")
        song = take_command()
        if song:
            play_youtube_music(song)
    elif "exit" in command or "quit" in command:
        speak("Thank you. Have a great day!")
        exit()
    elif "send message" in command:
        speak("What message do you want to send?")
        message = take_command()
        speak("To whom do you want to send the message?")
        number = take_command()
        if not number.startswith("+91"):
            number = "+91" + number
        pywhatkit.sendwhatmsg(number, message, datetime.datetime.now().hour, datetime.datetime.now().minute + 2)
    else:
        speak("I am not sure how to handle that request. Please try again.")

def wake_up_listener():
    """Continuously listen for the wake-up command."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for the wake-up command 'wake up'...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        while True:
            try:
                audio = recognizer.listen(source, timeout=None)
                command = recognizer.recognize_google(audio).lower()
                if "wake up" in command:
                    print("Wake-up command detected!")
                    speak("Yes, I am here!")
                    wishMe()
                    main_loop()
            except sr.UnknownValueError:
                continue
            except sr.RequestError as e:
                print(f"Speech recognition service error: {e}")
                break

def main_loop():
    """Main loop to handle user commands."""
    while True:
        print("Listening for your command...")
        command = take_command()
        if command:
            execute_command(command)
        else:
            speak("No valid command recognized. Please try again.")

if __name__ == "__main__":
    wake_up_listener()
