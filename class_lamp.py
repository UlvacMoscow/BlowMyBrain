class Lamp:

    def __init__(self):
        self.color = {1 : "Green", 2: "Red", 3: "Blue", 4: "Yellow"}
        self.count = 0

    def light(self):
        self.count += 1
        if self.count > 4:
            self.count = 1
        return self.color[self.count]



lamp_1 = Lamp()
lamp_2 = Lamp()

lamp_1.light() #Green
lamp_1.light() #Red
lamp_2.light() #Green

lamp_1.light() # "Blue"
lamp_1.light() # "Yellow"
lamp_1.light() # "Green"
lamp_2.light() # "Red"
lamp_2.light() # "Blue"
