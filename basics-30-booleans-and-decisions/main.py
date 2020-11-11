# Boolean type of variable can be only True or False

isSunny = True
isWind = False
temperature = 20

# logic operations on Boolean variables: not, and, or

isWeatherGood = temperature > 15 or (isSunny and not isWind)

if isWeatherGood:
    print("Go out")
else:
    print("Stay home")

temperature = 32
if temperature > 30:
    print("It's really hot outside!")

# nested if operator

isHomeworkDone = False

if isWeatherGood:
    if isHomeworkDone:
        print("Go out")
    else:
        print("Mom doesn't let me go")
else:
    print("Stay home")

# elif clause - additional condition

isSchoolTime = False

if isSchoolTime:
    print("Go to school")

elif isWeatherGood:
    if isHomeworkDone:
        print("Go out")
    else:
        print("Mom doesn't let me go")
else:
    print("Stay home")
