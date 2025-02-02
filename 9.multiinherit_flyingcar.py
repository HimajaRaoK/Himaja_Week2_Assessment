'''9. Simulate multiple inheritance where `FlyingCar` inherits from both `Car` and `Airplane`. 
Handle potential conflicts in the `move()` method.'''

class Car():
    def __init__(self,brand):
        self.brand=brand

    def drive(self):
        print(f"{self.brand} runs on the road")

class Airplane():
    def __init__(self,color):
        self.color=color

    def fly(self):
        print(f"{self.brand} airplane flys in the air")

class FlyingCar(Car,Airplane):
    def __init__(self,brand,color):
        Car.__init__(self,brand)
        Airplane.__init__(self,color)

    def drive_fly(self):
        print(f"{self.brand} is a flying {self.color} car")
        self.drive()
        self.fly()

flying_car=FlyingCar("Indigo","RED")
flying_car.drive_fly()

