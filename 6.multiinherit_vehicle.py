''' 6. Implement a multi-level inheritance example where `Vehicle` is a base class,
 `Car` and `Bike` inherit from `Vehicle`, and `ElectricCar` inherits from `Car`. '''

class Vehicle():
    def __init__(self,model):
        self.model=model
        pass
    
class Car(Vehicle):
    def __init__(self,model,color):
        super().__init__(model)
        self.color=color
        print(f"{model} is a Car and is of {color} color")
    
class Bike(Vehicle):
    def __init__(self,model,speed):
        super().__init__(model)
        self.speed=speed
        print(f"{model} is a Bike and has {speed} speed")
    
class ElectricCar(Car):
    def __init__(self,model,color,battery_life):
        super().__init__(model,color)
        self.battery_life=battery_life
        print(f"{model} is an EV and has a battery life of {battery_life} hours")
    
car = Car("Swift", "Red")
bike = Bike("Royal Enfield", "300 km/h")
electric_car = ElectricCar("Ola", "Black", 12)
    

    
