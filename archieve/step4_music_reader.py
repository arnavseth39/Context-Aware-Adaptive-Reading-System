import time
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Map context → music file
music_map = {
    "action": "assets/music/action.mp3",
    "dialogue": "assets/music/dialogue.mp3",
    "suspense": "assets/music/suspense.mp3",
    "narrative": "assets/music/narrative.mp3"
}

# Sample processed data (replace later with real data)
processed_data = [
    {"chunk": "He walked slowly into the dark room. The silence was unsettling.", "context": "suspense"},
    {"chunk": "Suddenly, footsteps approached rapidly and he began to run.", "context": "action"},
]

def play_music(context):
    try:
        pygame.mixer.music.load(music_map[context])
        pygame.mixer.music.play()
    except Exception as e:
        print(f"Music error: {e}")

def simulate_reading(data):
    total_words = 0
    start_time = time.time()

    print("\n--- START READING ---\n")

    for item in data:
        chunk = item["chunk"]
        context = item["context"]

        words = chunk.split()
        total_words += len(words)

        print(f"\nTEXT: {chunk}")
        print(f"CONTEXT: {context}")

        # play music based on context
        play_music(context)

        time.sleep(3)

    end_time = time.time()

    total_time_minutes = (end_time - start_time) / 60
    wpm = total_words / total_time_minutes

    print("\n--- READING COMPLETE ---")
    print(f"Total Words: {total_words}")
    print(f"Estimated WPM: {int(wpm)}")

simulate_reading(processed_data)