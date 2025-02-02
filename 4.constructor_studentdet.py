'''4. Implement a `Student` class with a constructor that initializes `name` and `roll_number`. 
Write a method to return student details.'''

class Student():
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def disp(self):
        print(f"Name: {self.name}, Roll Number: {self.roll}")
    
student=Student("Hima","1209")
student.disp()