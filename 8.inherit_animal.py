'''8. Design a system where a base class `Animal` 
has a method `speak()`, and subclasses `Dog` and `Cat` override it.'''

class Animal():
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"
    
d=Dog()
c=Cat()

print("Dog: ",d.speak())
print("Cat: ",c.speak())
    

       