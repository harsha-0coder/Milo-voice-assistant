# Milo voice assistant
Milo is a Python-based voice assistant that listens for a wake-up command and performs various tasks such as searching Wikipedia, playing music from YouTube, sending WhatsApp messages, and performing Google searches.

This project demonstrates how speech recognition, text-to-speech, and automation can be combined to create a personal AI assistant.

The assistant activates when it hears the phrase:
### wake up
After activation, Milo listens for commands and executes them.
## Features

Milo currently supports the following commands:

1.  Wake Word Detection

Continuously listens for "wake up"

Activates the assistant when detected

2.  Text to Speech

Uses pyttsx3 for offline speech synthesis

3.  Wikipedia Search

Example command:

### wikipedia artificial intelligence

Milo will read the summary from Wikipedia.

4. Google Search

Example command:

5. search google
Play Music from YouTube

Example command:

play music

Milo will ask which song to play and open it on YouTube.

6.  Send WhatsApp Message

Example command:

send message

Milo will ask:

Message content

Phone number

Then it sends the message using pywhatkit.

7. Introduction

Example command:

introduce yourself

Milo will introduce itself.

8. Exit

Example command:

exit

Stops the assistant.

## How Milo Works

The microphone continuously listens for the phrase "wake up".

When detected, Milo greets the user.

It then listens for commands.

The command is converted from speech → text.

The program executes the corresponding function.

Technologies used:

Speech Recognition

Text To Speech

Python Automation

Web APIs
