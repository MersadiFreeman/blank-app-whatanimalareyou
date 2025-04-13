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
        "question": "What's your hobby?",
        "answer": {
            "a": ("Family time is my favorite.", "Penguin"),
            "b": ("Hiking", "Bear"),
            "c":
