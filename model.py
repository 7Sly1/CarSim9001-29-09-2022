from random import randint

class Car(object):
    def __init__(self):
        # Erklærer instansvariable for: "self.theEngine".
        self.theEngine = Engine()
    # Metoden "updateModel" i "Car" laves her.
    def updateModel(self, dt):
        self.theEngine.updateModel(dt)


class Wheel(object):
    # Erklærer instansvariable for: "self.orientation".
    def __init__(self):
        # self.orientation er her de 4 hjuls tilfældige start position når programmet starter.
        self.orientation = randint(0,360)

    # Metoden "rotate" i "Wheel" laves her.
    def rotate(self, revolutions):
        # "degreesOfRotation" er en variable for, hvor meget de 4 hjul har drejet sig når bilen kører.
        degreesOfRotation = 360 * revolutions
        # "self.orientation" bruges her til at holde styr på de 4 hjuls rotation, når programmet kører.
        self.orientation = (self.orientation + degreesOfRotation) % 360


class Engine(object):
    # Erklærer instansvariable for: "self.throttlePosition", "self.theGearbox", "self.currentRpm",
    # "self.consumptionConstant", "self.maxRpm" og "self.theTank"
    def __init__(self):
        self.throttlePosition = 0
        self.theGearbox = Gearbox()
        self.currentRpm = 0
        self.consumptionConstant = 0.0025
        self.maxRpm = 100
        self.theTank = Tank()

    # Metoden "UpdateModel" i "Engine" laves her.
    def updateModel(self, dt):
        # Her sætte de værdi, der skal være tilstede for at bilen kan kører.
        if self.theTank.contents > 0:
            self.currentRpm = self.throttlePosition * self.maxRpm
            self.theTank.remove(self.currentRpm * self.consumptionConstant)
            self.theGearbox.rotate(self.currentRpm * (dt / 60))
        else:
            # Hvis ikke alle værdier er til skal "self.currentRpm" være 0. Altså at bilen kører ikke nogen steder.
            self.currentRpm = 0


class Gearbox(object):
    # Erklærer instansvariable for: "self.wheels", "self.wheels",
    # "self.currentGear", "self.clutchEngaged" og "self.contents".
    def __init__(self):
        # "self.wheels" er en variable til et tomt "dictionary".
        self.wheels = {}
        # For loopet "newWheel", oprette det 4 hjul på bilen.
        for newWheel in ['frontLeft', 'frontRight', 'rearLeft', 'rearRight']:
            # Det tomme "dictionary" "self.wheels = "newWheel",
            # det betyder at de 4 hjul bliver sat ind i "dictionary'et"
            self.wheels[newWheel] = Wheel()
        # "self.currentGear" er hvilket gear bilen er i lige nu.
        self.currentGear = 0
        # "self.clutchEngaged" tjekker om koblingen er trykket ned eller ej. Altså om gear skift er muligt.
        self.clutchEngaged = False
        self.gears = [0, 0.8, 1, 1.4, 2.2, 3.8]

    # Metoden "shiftUp" i "Gearbox" laves her.
    def shiftUp(self):
        # Her tjekkes der for om "self.currentGear" kan gå 1 gear op,
        # hvis "self.currentGear" < end længden af "self.gears" - 1
        # (- 1 er med for at gøre det muligt komme i sidste gear) og "self.clutchEngaged" er = True.
        if self.currentGear < len(self.gears) - 1 and not self.clutchEngaged:
            # Sætter "self.currentGear" 1 op.
            self.currentGear += 1

    # Metoden "shiftDown" i "Gearbox" laves her.
    def shiftDown(self):
        # Her tjekkes der for om "self.currentGear" kan gå 1 gear ned,
        # hvis "self.currentGear" > 0, og "self.clutchEngaged" er = True.
        if self.currentGear > 0 and not self.clutchEngaged:
            # Sætter "self.currentGear" 1 ned.
            self.currentGear -= 1

    # Metoden "rotate" i "Gearbox" laves her.
    def rotate(self, revolutions):
        # Hvis "self.clutchEngaged" er false.
        if self.clutchEngaged:
            # Så vil "newRevs" være = "revolutions" * "self.gears[self.currentGear]".
            newRevs = revolutions * self.gears[self.currentGear]
            # For hvert hjul i "self.wheels", vil få samme antal "newRevs" og derfor rotere samme antal grader.
            for wheel in self.wheels:
                self.wheels[wheel].rotate(newRevs)


class Tank(object):
    # Erklærer instansvariable for: "self.capacity" of "self.contents".
    def __init__(self):
        self.capacity = 100
        self.contents = 100

    # Metoden "remove" i "Tank" laves her.
    def remove(self, amount):
        # "self.contents" -= "self.amount": Er tankens størrelse minus det brændstof der bliver brugt når bilen kører.
        self.contents -= amount
        # Derudover tjekkes der også for, hvornår "self.contents" < 0 og sætter den til = 0,
        # da tankens størrelse ikke kan gå i minus.
        if self.contents < 0:
            self.contents = 0

    # Metoden "refuel" i "Tank" laves her.
    def refuel(self):
        # Når bilen genfyldes, så skal "self.contents" og "self.capacity" være lig det samme.
        self.contents = self.capacity