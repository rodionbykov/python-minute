from dino import Dino

# dinosaurs are kept on leash, going around the pole
# if two dinosaurs meet, they eat (or marry) each other

dino1 = Dino()
dino1.name = "Barsik"
dino1.center_x = 8
dino1.center_y = 3
dino1.radius = 2.5


dino2 = Dino()
dino2.name = "Sharik"
dino2.center_x = 5
dino2.center_y = 6
dino2.radius = 3


dino3 = Dino()
dino3.name = "Shurik"
dino3.center_x = 11
dino3.center_y = 5
dino3.radius = 2.5


dino4 = Dino()
dino4.name = "Serij"
dino4.center_x = 4
dino4.center_y = 8
dino4.radius = 2


dinosaurs = [dino1, dino2, dino3, dino4]


for dino in dinosaurs:
    for friend in dinosaurs:
        if dino != friend:
            if dino.check(friend):
                print(f"LOVE {dino.name} and {friend.name}")
            else:
                print(f"NO LOVE {dino.name} and {friend.name}")
