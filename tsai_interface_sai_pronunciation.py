
from gtts import gTTS
import pygame
import time
import os

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("response.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.5)

def process_input(user_input):
    user_input = user_input.lower()

    if "your name" in user_input:
        return "I am Sai, your Temporal Synthetic Autonomous Intelligence."
    elif "time" in user_input:
        return f"The current time is {time.strftime('%I:%M %p')}."
    elif "joke" in user_input:
        return "Why did the AI cross the road? To optimize the chicken's path!"
    elif "exit" in user_input:
        return "Goodbye, Captain."
    else:
        return "I'm not sure how to respond to that yet."

# --- Main loop ---
pygame.init()
speak("Sai online. Awaiting your command.")

while True:
    user_input = "What is your name?"  # Replace with input() if needed
    print("You:", user_input)
    response = process_input(user_input)
    print("Sai:", response)
    speak(response)

    if "goodbye" in response.lower():
        break
