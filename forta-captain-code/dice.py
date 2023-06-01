import random
def get_stars(num_die):
    if num_die < 1 and num_die > 6:
        return ""

    result = ""
    i = 0
    while i < num_die:
        result = result + "*"
        i = i+1
    return result

die1_human = random.randrange(1,7)
die2_human = random.randrange(1,7)

die1_robot = random.randrange(1,7)
die2_robot = random.randrange(1,7)

stars1_human = get_stars(die1_human)
stars2_human = get_stars(die2_human)

stars1_robot = get_stars(die1_robot)
stars2_robot = get_stars(die2_robot)

if (die1_human + die2_human) > (die1_robot + die2_robot):
    print(f"You rolled {stars1_human} and {stars2_human}. Robot rolled {stars1_robot} and {stars2_robot}. You win!" )
elif (die1_human + die2_human) < (die1_robot + die2_robot):
    print(f"You rolled {stars1_human} and {stars2_human}. Robot rolled {stars1_robot} and {stars2_robot}. Robot wins!" )
else:
    print(f"You rolled {stars1_human} and {stars2_human}. Robot rolled {stars1_robot} and {stars2_robot}. It's a tie." )

if (die1_human + die2_human) == 2 or (die1_robot + die2_robot) == 2:
    print("SNAKE EYES!")
    
if (die1_human + die2_human) == 11 or (die1_robot + die2_robot) == 11:
    print("YO-LEVEN!")
    
if (die1_human + die2_human) == 12 or (die1_robot + die2_robot) == 12:
    print("MIDNIGHT!")

if (die1_human == 2 and die2_human == 2) or (die1_robot == 2 and die2_robot == 2):
    print("LITTLE JOE!")

if (die1_human == 4 and die2_human == 4) or (die1_robot == 4 and die2_robot == 4):
    print("SQUARE PAIR!")
