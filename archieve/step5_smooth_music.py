import time
import pygame
from collections import deque

# Initialize pygame mixer
pygame.mixer.init()

# Map context → music file
music_map = {
    "action": "assets/music/action.mp3",
    "dialogue": "assets/music/dialogue.mp3",
    "suspense": "assets/music/suspense.mp3",
    "narrative": "assets/music/narrative.mp3"
}

# Sample processed data (replace later)
processed_data = [
    {"chunk": "He walked slowly into the dark room. The silence was unsettling.", "context": "suspense"},
    {"chunk": "A sudden noise echoed behind him and he turned quickly.", "context": "action"},
    {"chunk": "The silence returned again, deeper than before.", "context": "suspense"},
    {"chunk": "Suddenly, footsteps approached rapidly and he began to run.", "context": "action"},
]

def play_music(context):
    try:
        pygame.mixer.music.load(music_map[context])
        pygame.mixer.music.play(-1)  # loop music
    except Exception as e:
        print(f"Music error: {e}")

def get_stable_context(history):
    return max(set(history), key=history.count)

def simulate_reading(data):
    history = deque(maxlen=3)
    current_music = None
    cooldown_counter = 0

    print("\n--- START READING ---\n")

    for item in data:
        chunk = item["chunk"]
        context = item["context"]

        print(f"\nTEXT: {chunk}")
        print(f"RAW CONTEXT: {context}")

        # Update history
        history.append(context)

        # Get stable context
        if len(history) == 3:
            stable_context = get_stable_context(list(history))
        else:
            stable_context = context

        print(f"STABLE CONTEXT: {stable_context}")

        # 🔥 FIXED LOGIC

        # First time → play immediately
        if current_music is None:
            print(f"🎵 Starting music → {stable_context}")
            play_music(stable_context)
            current_music = stable_context
            cooldown_counter = 0

        # Change music only if stable + cooldown passed
        elif stable_context != current_music and cooldown_counter >= 2:
            print(f"🎵 Switching music → {stable_context}")
            pygame.mixer.music.fadeout(1000)  # smooth fade out
            play_music(stable_context)
            current_music = stable_context
            cooldown_counter = 0

        else:
            cooldown_counter += 1

        time.sleep(3)

simulate_reading(processed_data)