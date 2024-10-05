import random

print("----------")
print("Task #1")

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
time_of_day = ["morning", "afternoon", "evening"]
moods = ["happy", "sad", "angry", "anxious", "excited", "calm", "bored"]

for day in days:
    for time in time_of_day:
        random_mood = random.choice(moods)
        print(f"On {day} {time} you were {random_mood}.")
        print("----------")