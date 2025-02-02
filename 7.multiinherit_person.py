''' 7. Create a multi-level class structure with `Person` → `Employee` → `Manager`,
 where `Manager` has an additional method `approve_leave()`. '''

class Person():
    def __init__(self,category):
        self.category=category
        print(f"Im a {category}")

class Employee(Person):
    def __init__(self,category):
        super().__init__(category)

class Manager(Person):
    def __init__(self,category,approve_leave):
        super().__init__(category)
        self.approve_leave=approve_leave
        print(f"I also {approve_leave} of employees")

employee = Employee("Employee")
manager = Manager("Manager", "approve leaves")



