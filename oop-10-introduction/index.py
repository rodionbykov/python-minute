
class Cat:
    pass

cat = Cat()

print(cat)

class FancyCat():
    description = "Not a stray cat"
    def __init__(self, breed):
        self.breed = breed
    
    # instance method
    def say(self, text):
        print(f"Cat says {text}")

    # special instance method
    def __str__(self) -> str:
        return f"I am {self.description}, {self.breed}"

    # also 
    # __eq__ for comparison

maincoon = FancyCat('Maine Coon')

print(FancyCat.description)
print(maincoon.description)
print(maincoon.breed)

FancyCat.description = "Cool cat"
print(FancyCat.description)
print(maincoon.description)

maincoon.description = "Big cat"
print(FancyCat.description)
print(maincoon.description)

maincoon.lapki = 4
# print(FancyCat.lapki)
print(maincoon.lapki)

FancyCat.ushki = 2
print(FancyCat.ushki)
print(maincoon.ushki)

if isinstance(maincoon, FancyCat):
    print("maincoon is a fancy cat")

maincoon.say("meow")
print(maincoon)

print(dir(maincoon))