import random

print("----------")
print("Task #1")

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
moods = ["happy", "sad", "angry", "anxious", "excited", "calm", "bored"]

for day in days:
    random_mood = random.choice(moods)
    print(f"On {day}, you were feeling {random_mood}.")
    print("----------")