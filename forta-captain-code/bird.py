import random

class Bird:
    kind = "simple bird"
    name = ""
    color = ""
    foot = 2
    wing = 2

    def fly(self):
        num1 = random.randrange(0,3)
        if num1 == 0:
            print(f"Baaaaah, I felt")
        else:
            print(f"I'm flying")

    def groan(self):
        print(f"groan squawk groan squawk")

    def __str__(self) -> str:
        return f"Hello, I'm {self.name}, {self.kind} of color {self.color}"


class Crow(Bird):
    kind = "Crow"
    def groan(self):
        print(f"CAR CAR CAR!!!!!!!!!")
    def fly(self):
        print(f"I'm flying, ALWAYS")


class Cockatoo(Bird):
    kind = "Cockatoo"
    color = "white"

    def fly(self):
        print(f"I'm magestically flying")
    
    def talk(self, word):
        num1 = random.randrange(0,3)
        if num1 == 0:
            self.groan()
        else:
            print(f"{word}, {word}, {word} lol")
        