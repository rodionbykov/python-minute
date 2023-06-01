def tight_screw(num_screw):
    print("Tighten the screw ", num_screw)

def loose_screw(num_screw):
    print(f"Loosen the screw {num_screw}")

def wheel_off(wheel):
    print(f"Taking wheel {wheel} off:")
    for screw in range(1,6):
        loose_screw(screw)

def wheel_on(wheel):
    print(f"Placing {wheel} back on:")
    for screw in range(1,6):
        tight_screw(screw)

def prepare(list_of_things):
    for thing in list_of_things:
        print(f"I take {thing}")

def lift(car, thing):
    print(f"Lift a {car} using {thing}")

def down(car, thing):
    print(f"Putting {car} down using {thing}")

car = "FORD"

key = "KEY"
jack = "JACK"
wheel = "BAD WHEEL"
spare = "SPARE WHEEL"

things = [key, jack, wheel, spare]

print("Preparing:")
prepare(things)
lift(car, jack)
wheel_off(wheel)
wheel_on(spare)
down(car, jack)
print("Car is ready")
