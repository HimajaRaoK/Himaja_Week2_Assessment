'''10. Build a `SmartPhone` class inheriting from `MobileDevice`,
 which in turn inherits from `Electronics`. 
Demonstrate method overriding and attribute reuse.'''

class Electronics():
    def device_type(self,brand):
        self.brand=brand
        return (f"Brand: {self.brand} - Electronics")
    
class MobileDevice(Electronics):
    def device_type(self, brand):
        self.brand=brand
        return (f"Brand: {self.brand} - Mobile Device")

class SmartPhone(MobileDevice):
    def device_type(self, brand):
        self.brand=brand
        return (f"Brand: {self.brand} - Smart Phone")
    
phone=SmartPhone()
print(phone.device_type("Samsung"))
        




