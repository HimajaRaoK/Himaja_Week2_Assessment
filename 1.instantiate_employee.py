'''1. Create a class `Employee` with properties `name`, `id`, and `department`. 
Instantiate an object and assign values dynamically.'''

class Employee:
    def __init__(self,name,id,dept):
        self.name=name
        self.id=id
        self.dept=dept

    def display(self):
        print(f"Employee name is {self.name}")
        print(f"Employee id is {self.id}")
        print(f"Department is {self.dept}")

name=input("Enter employee name:")
id=int(input("Enter employee ID:"))
dept=input("Enter department:")

employee=Employee(name,id,dept)

employee.display()
