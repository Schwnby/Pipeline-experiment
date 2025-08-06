from enum import Enum

class Timmy:
    def __init__(self):
        self.mood = Mood.Happy

    def set_mood_happy(self):
        self.mood = Mood.Happy

    def set_mood_sad(self):
        self.mood = Mood.Sad

    def set_mood_angry(self):
        self.mood = Mood.Angry

    def set_mood_confused(self):
        self.mood = Mood.Confused

    def how_is_timmy(self):
        print("Timmy is very" + self.mood.name + "right now")

class Mood(Enum):
    Happy = 0
    Sad = 0
    Angry = 0
    Confused = 0