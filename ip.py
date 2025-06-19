import json
import os

def load_memory():
    if os.path.exists("memory.json"):
        with open("memory.json", "r") as f:
            return json.load(f)
    return {"last_input": "", "knowledge": {}, "mood": "neutral"}

def save_memory(memory):
    with open("memory.json", "w") as f:
        json.dump(memory, f, indent=2)
