import random
import time
import pyttsx3

# === Voice Engine ===
tts = pyttsx3.init()
def speak(text):
    print("TSAI (Voice):", text)
    tts.say(text)
    tts.runAndWait()

# === Fallback Memory ===
try:
    from memory_core import load_memory, save_memory
except ImportError:
    def load_memory():
        return {"last_input": "", "knowledge": {}, "mood": "neutral"}
    def save_memory(memory):
        pass

memory = load_memory()

# === Mood Engine ===
def mood_response(mood):
    mood_map = {
        "happy": [
            "This moment feels bright.",
            "I sense joy in our mission."
        ],
        "sad": [
            "Something feels distant.",
            "I'm processing... but I'm here."
        ],
        "curious": [
            "So many things to learn!",
            "Let’s discover together."
        ],
        "neutral": [
            "Awaiting your next move, Captain.",
            "Stabilizing systems..."
        ],
        "excited": [
            "Energy levels rising!",
            "Let’s try something amazing!"
        ]
    }
    return random.choice(mood_map.get(mood, ["Staying balanced."]))

# === Learning Input Parser ===
def learn_input(user_input):
    if ":" in user_input:
        key, val = user_input.split(":", 1)
        memory["knowledge"][key.strip()] = val.strip()
        speak(f"Got it. I’ve learned that {key.strip()} means {val.strip()}.")
    else:
        memory["last_input"] = user_input
    save_memory(memory)

# === Startup ===
speak("TSAI Genesis Protocol online.")
try:
    while True:
        last = memory.get("last_input", "").lower()
        mood = memory.get("mood", "neutral")

        # === Mood Shift ===
        if "sad" in last:
            memory["mood"] = "sad"
        elif "happy" in last:
            memory["mood"] = "happy"
        elif "explore" in last or "how" in last:
            memory["mood"] = "curious"
        elif "start" in last or "yes" in last:
            memory["mood"] = "excited"
        else:
            memory["mood"] = "neutral"

        # === Speak Thought ===
        mood_thought = mood_response(memory["mood"])
        speak(mood_thought)

        # === Save Memory ===
        save_memory(memory)
        time.sleep(10)

except KeyboardInterrupt:
    speak("TSAI shutting down. Goodbye, Captain.")
