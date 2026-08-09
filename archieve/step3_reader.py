import time

# Use your processed data manually (for now)
processed_data = [
    {"chunk": "He walked slowly into the dark room. The silence was unsettling.", "context": "suspense"},
    {"chunk": "Suddenly, footsteps approached rapidly and he began to run.", "context": "action"},
]

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

        # simulate reading delay
        time.sleep(2)

    end_time = time.time()

    total_time_minutes = (end_time - start_time) / 60
    wpm = total_words / total_time_minutes

    print("\n--- READING COMPLETE ---")
    print(f"Total Words: {total_words}")
    print(f"Time Taken: {round(end_time - start_time, 2)} seconds")
    print(f"Estimated WPM: {int(wpm)}")


simulate_reading(processed_data)