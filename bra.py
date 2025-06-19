import subprocess
import sys
import random
import time

# Auto-install helper
def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

try:
    from memory_core import load_memory, save_memory
except ImportError:
    print("[Warning] memory_core.py not found. Using dummy memory.")
    def load_memory():
        return {}
    def save_memory(memory):
        pass

# Idea generator
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
        print
