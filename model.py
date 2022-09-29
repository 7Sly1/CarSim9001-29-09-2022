from random import randint

class Car(object):
    pass

class Wheel(object):
    def __init__(self):
        self.orientation = randint(0,360)

    def rotate(self, revolutions):
        degreesOfRotation = 360 * revolutions
        self.orientation = (self.orientation + degreesOfRotation) % 360

class Engine(object):
    pass

class Gearbox(object):
    pass

class Tank(object):

    def __init__(self):
        self.capacity = 100
        self.contents = 100

    def remove(self, amount):
        self.contents -= amount
        if self.contents < 0:
            self.contents = 0

    def refuel(self):
        self.contents = self.capacity