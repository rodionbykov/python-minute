from bird import Bird, Crow, Cockatoo

crow1 = Crow()
crow1.name = "Kruk"
crow1.color = "black"
print(crow1)

crow1.fly()
crow1.groan()

parrot1 = Cockatoo()
parrot1.name = "Stepan"
print(parrot1)

parrot1.fly()
parrot1.groan()

while True:
    word = input("Talk with me:")
    parrot1.talk(word)
