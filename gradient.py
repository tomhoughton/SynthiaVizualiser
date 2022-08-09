class Gradient:
    def __init__(self, startColor: tuple, endColor: tuple, isVerticle: bool, distance: int) -> None:
        self.startColor = startColor
        self.endColor = endColor
        self.isVerticle = isVerticle
        self.distance = distance
        self.m = None
        self.increaseOrDecrease = [False, False, False] # In RGB, decides if the value increases or not

    def obtainM(self): 
        self.m = 255 / self.distance

    def cacl_increase(self):
        
        # # THIS IS REPEATING CODE!!! LOOP IT
        # # Red:
        # if (self.startColor[0] < self.endColor[1]):
        #     self.increaseOrDecrease[0] = True
        # else:
        #     self.increaseOrDecrease[0] = False

        # # Green:
        # if (self.startColor[1] < self.endColor[1]):
        #     self.increaseOrDecrease[1] = True
        # else:
        #     self.increaseOrDecrease[1] = False

        # # Blue:
        # if (self.startColor[2] < self.endColor[2]):
        #     self.increaseOrDecrease[2] = True
        # else:
        #     self.increaseOrDecrease[2] = False

        for i, val in enumerate(self.increaseOrDecrease):
            if (self.startColor[i] < self.endColor[i]):
                self.increaseOrDecrease[i] = True
            else:
                self.increaseOrDecrease[i] = False



    
    def linear_normal(self, x):
        return x * self.m

    def linear_inverse(self, x):
        c = 255
        return (x * -(self.m)) + c

    def calculate_color(self, x_coord: int, y_coord: int):
        rgb = []
        
        for x in self.increaseOrDecrease:
            if (x == True):
                rgb.append(int(self.linear_normal(x=x_coord)))
            else:
                rgb.append(int(self.linear_inverse(x=x_coord)))

        return tuple(rgb)