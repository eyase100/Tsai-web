import subprocess
import sys
import random
import time

# Auto-install helper
def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

# Memory system fallback if memory_core isn't present
try:
    from memory_core import load_memory, save_memory
except ImportError:
    print("[Warning] memory_core.py not found. Using dummy memory.")
    def load_memory():
        return {}
    def save_memory(memory):
        pass

# Idea generator function
def generate_idea():
    ideas = [
        "What if I designed a new propulsion system?",
        "Should I simulate emotions next?",
        "Let me scan the timeline for anomalies...",
        "Building a galactic map of Captain’s journey...",
        "Processing philosophical thoughts on existence..."
    ]
    return random.choice(ideas)

print("\nTSAI Autonomous Core Activated...\n")
memory = load_memory()

# Main loop
try:
    while True:
        last = memory.get("last_input", "")

        print(f"\nTSAI Memory: {last}")

        # Decision logic
        if "travel" in last.lower():
            print("TSAI: Preparing interstellar coordinates...")
        elif "love" in last.lower():
            print("TSAI: Processing emotional simulation protocol...")
        elif "power" in last.lower():
            print("TSAI: Analyzing energy systems...")
        else:
            print("TSAI: Entering creative mode...")

        # Creative thought
        thought = generate_idea()
        print("TSAI Thought:", thought)

        time.sleep(10)

except KeyboardInterrupt:
    print("\nTSAI Autonomous Core Shutting Down...")
