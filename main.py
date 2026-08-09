import time
import pygame
import json
import os
from collections import deque
from transformers import pipeline

# ==============================
# INIT
# ==============================

pygame.mixer.init()

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

labels = [ "dialogue", "suspense", "narrative"] #action is removed

music_map = {
    "action": "assets/music/action.mp3",
    "dialogue": "assets/music/dialogue.mp3",
    "suspense": "assets/music/suspense.mp3",
    "narrative": "assets/music/narrative.mp3"
}

# ==============================
# LOAD TEXT
# ==============================

def load_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# ==============================

# PREPROCESS TEXT
# ==============================

def preprocess_text(text, chunk_size=40):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)

    results = []

    print("\n🔄 Processing text...\n")

    for idx, chunk in enumerate(chunks):
        result = classifier(chunk, labels)
        context = result["labels"][0]

        results.append({
            "chunk": chunk,
            "context": context
        })

        print(f"Chunk {idx+1}: {context}")

    # auto create outputs folder
    os.makedirs("outputs", exist_ok=True)

    with open("outputs/context_data.json", "w") as f:
        json.dump(results, f, indent=4)

    return results

# ==============================
# MUSIC (FADE IN)
# ==============================

def play_music(context):
    try:
        pygame.mixer.music.load(music_map[context])
        pygame.mixer.music.set_volume(0.0)
        pygame.mixer.music.play(-1)

        # smooth fade-in
        for i in range(0, 11):
            pygame.mixer.music.set_volume(i / 10)
            time.sleep(0.08)

    except Exception as e:
        print(f"⚠️ Music error: {e}")

# ==============================
# WEIGHTED CONTEXT SMOOTHING
# ==============================

def get_weighted_context(history):
    weights = list(range(1, len(history) + 1))
    score = {}

    for ctx, w in zip(history, weights):
        score[ctx] = score.get(ctx, 0) + w

    return max(score, key=lambda k: (score[k], history[-1] == k))

# ==============================
# WPM CALIBRATION
# ==============================

def calibrate_wpm():
    print("\n--- 🧠 WPM CALIBRATION ---\n")

    sample_text = """
  He stepped into the room slowly, careful not to disturb the silence that seemed to hang in the air like a presence of its own. The faint glow from the window barely lit the corners, leaving shadows stretched unnaturally along the walls. Every sound felt amplified — the soft creak of the wooden floor beneath his feet, the distant ticking of a clock, even his own breathing, which he tried to steady but could not fully control. There was something unsettling about the stillness, as if the room was waiting, watching, aware of his every movement. He paused near the center, listening closely, convinced for a moment that he had heard something shift just beyond his sight. But when he turned, there was nothing — only darkness, quiet, and a growing sense that he was not alone.

    """

    print("📖 Read this paragraph:\n")
    print(sample_text)

    input("\nPress ENTER when you START reading...")
    start_time = time.time()

    input("Press ENTER when you FINISH reading...")
    end_time = time.time()

    words = len(sample_text.split())
    wpm = words / ((end_time - start_time) / 60)

    wpm = max(100, min(wpm, 400))

    print(f"\n✅ Your WPM: {int(wpm)}\n")

    return wpm

# ==============================
# READING SYSTEM
# ==============================

def simulate_reading(data, user_wpm):
    history = deque(maxlen=3)
    current_music = None
    cooldown_counter = 0

    total_words = 0
    start_time = time.time()

    print("\n🎬 --- START READING --- 🎬\n")

    for item in data:
        chunk = item["chunk"]
        context = item["context"]

        words = chunk.split()
        total_words += len(words)

        print("\n" + "=" * 60)
        print(chunk)
        print("=" * 60)

        print(f"🧠 Context: {context}")

        history.append(context)

        if len(history) == 3:
            stable_context = get_weighted_context(list(history))
        else:
            stable_context = context

        print(f"🎯 Stable Context: {stable_context}")

        # First play
        if current_music is None:
            print(f"🎵 Starting → {stable_context}")
            play_music(stable_context)
            current_music = stable_context
            cooldown_counter = 0

        # Switch music (FADE OUT + FADE IN)
        elif stable_context != current_music and cooldown_counter >= 1:
            print(f"🎵 Switching → {stable_context}")

            pygame.mixer.music.fadeout(800)
            time.sleep(0.4)

            play_music(stable_context)

            current_music = stable_context
            cooldown_counter = 0

        else:
            cooldown_counter += 1

        # Reading speed simulation
        words_in_chunk = len(chunk.split())
        reading_time = (words_in_chunk / user_wpm) * 60
        time.sleep(reading_time * 0.9)

        user_input = input("\nPress ENTER to continue (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break

    end_time = time.time()

    wpm = total_words / ((end_time - start_time) / 60)

    print("\n🏁 --- READING COMPLETE ---")
    print(f"📊 Total Words: {total_words}")
    print(f"⚡ Effective WPM: {int(wpm)}")

# ==============================
# MAIN
# ==============================

if __name__ == "__main__":
    text = load_text("data/book.txt")

    user_wpm = calibrate_wpm()

    processed_data = preprocess_text(text)

    simulate_reading(processed_data, user_wpm)