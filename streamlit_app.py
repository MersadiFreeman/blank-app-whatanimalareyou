import streamlit as st

st.title("What Animal Are You?")
st.write("Take this personality quiz to find out what animal you are with specific personality traits! Have fun!")
personalities = {
    "Bear": 0,
    "Dolphin": 0,
    "Owl": 0,
    "Penguin": 0,
    "Bat": 0,
}
questions = [
    {
        "question": "How do you spend your mornings?",
        "answers": {
            "a": ("Coffee first and foremost!", "Owl"),
            "b": ("I like to sleep in.", "Bear"),
            "c": ("Ugh!", "Bat"),
            "d": ("Ready to go!", "Penguin"),
            "e": ("Cold swim! Let's get the blood going!", "Dolphin")
        }
    },
    {
        "question": "What is your hobby?",
        "answers": {
            "a": ("Family time is my favorite.", "Penguin"),
            "b": ("Hiking", "Bear"),
            "c": ("I love to travel", "Owl"),
            "d": ("Party with friends.", "Dolphin"),
            "e": ("Sleeping.", "Bat")
        }
    },
    {
        "question": "Describe yourself briefly.",
        "answers": {
            "a": ("Loyal", "Penguin"),
            "b": ("Strong", "Bear"),
            "c": ("Inedpendent", "Owl"),
            "d": ("Easy going!", "Dolphin"),
            "e": ("Party! The night is young!", "Bat")
        }
    },
    {
        "question": "Favorite time of day?",
        "answers": {
            "a": ("Mornings", "Penguin"),
            "b": ("Afternoons", "Bear"),
            "c": ("Night time.", "Owl"),
            "d": ("5pm?", "Bat"),
            "e": ("Anytime is a good time!", "Dolphin")
        }
    },
    {
        "question": "What's your season?",
        "answers": {
            "a": ("Summer. It's the best. Don't say otherwise.", "Dolphin"),
            "b": ("Spring and winter!", "Bear"),
            "c": ("Winter.", "Penguin"),
            "d": ("Fall. Like my prey...", "Owl"),
            "e": ("Anything, but the cold!", "Bat")
        }
    }
]
for q in questions:
    print("\n" + q["question"])
    for key, (text, _) in q["answers"].items():
        print(f" {key}) {text}")
    while True:
        answer = input("Your choice (a/b/c/d/e): ").lower()
        if answer in q["answers"]:
            chosen_personality = q["answers"][answer][1]
            personalities[chosen_personality] += 1
            break
        else:
            print("Please enter a valid option (a,b,c,d, or e).")
result = max(personalities, key=personalities.get)

descriptions = {
    "Bear": "You're a Bear! Strong, grounded, and you love your naps. You’re dependable and powerful, but also know when to chill.",
    "Dolphin": "You're a Dolphin! Social, playful, and full of energy. You bring joy to those around you and thrive in good company.",
    "Owl": "You're an Owl! Wise, curious, and independent. You enjoy deep thoughts and late nights under the stars.",
    "Penguin": "You're a Penguin! Loyal, family-oriented, and playful. You’re always looking out for your people.",
    "Bat": "You're a Bat! Mysterious, nocturnal, and maybe a little dramatic. You shine brightest when the sun goes down."
}
print("\n Your personality is:", result)
print(descriptions[result])
