import math

class Dino:
    name = ""
    radius = 0
    center_x = 0
    center_y = 0

    def check(self, d2):
        result = None
        sum_rad = self.radius + d2.radius
        distantion = math.sqrt(pow(self.center_y - d2.center_y, 2) + pow(self.center_x - d2.center_x, 2))
        if distantion > sum_rad:
         result = False
        else:
            result = True
            return result
