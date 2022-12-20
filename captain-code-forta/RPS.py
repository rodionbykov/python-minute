import random

name=input("What's your name?:").lower()

bet=input("Your bet:")
if bet.isdigit():
    bet_value = int(bet)
else:
    print("ok, sayonnara")
    exit()
c=random.choice("RPS")

print("Hello", name.capitalize(), "let's play Rock, paper, or scissors")
u=input('Enter R,P,S:').upper().strip()
print("you:",u)

# cheating
if name == "alice":
    if u == "R":
        c = "P"
    if u == "S":
        c = "R"
    if u == "P":
        c = "S"

# cheating even more
if name == "bob":
    if u == "R":
        c = "S"
    if u == "S":
        c = "P"
    if u == "P":
        c = "R"

print("computer", c)
w_value=bet_value*2
l_value=0
if c == u:
    print("It's a tie!")
elif u == "R" and c == "P":
    print("You lose!")
elif u == "P" and c == "R":
    print("You WIN! On your account is ", w_value  )
elif u == "R" and c == "S":
    print("You WIN!")
elif u == "S" and c == "R":
    print("You lose!")
elif u == "P" and c == "S":
    print("You lose!")
elif u == "S" and c == "P":
    print("You WIN!")
else:
    print("No, only R, P, S!")
