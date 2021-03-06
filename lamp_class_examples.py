class Lamp:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bright(self):
        return print('Lamp {} bright {}'.format(self.name, self.color))

    @classmethod
    def create_lamp(cls, data):
        name, color = data
        return cls(name, color)

    @staticmethod #work function не имеет доступ к переменным экземпляра
    def get_info(self):
        return print('Lamp {} bright {}'.format(self.name, self.color))


green_lamp = Lamp('Gr', 'green')
green_lamp.bright()

red_lamp_list = ['Rd', 'red']

red_lamp = Lamp.create_lamp(red_lamp_list)
red_lamp.bright()
red_lamp.get_info(green_lamp)
