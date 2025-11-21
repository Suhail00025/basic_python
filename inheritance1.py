class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(self.name, self.age)

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name,age)
        self.employee_id = employee_id

    def show_details(self):
        print(self.name, self.age, self.employee_id)

class ParTime(Person):
    def __init__(self, name, age, working_hours):
        super().__init__(name, age)
        self.working_hours = working_hours

    def show_details(self):
        print(self.name, self.age, self.working_hours)

class Consultant(Employee,ParTime):
    def __init__(self, name, age, employee_id, working_hours, project_name):
        Employee.__init__(self, name, age, employee_id)
        ParTime.__init__(self, name, age, working_hours)
        # super().__init__(name, age, employee_id, working_hours)
        self.project_name = project_name

    def show_details(self):
        print(self.name, self.age, self.employee_id, self.working_hours, self.project_name)
    

person_obj = Person("Alice", 30)
employee_obj = Employee("Bob", 40, "123")
partime_obj = ParTime("Charlie", 25, 20.5)
consultant_obj = Consultant("Diana", 35, "456", 15.0, "AI Project")

person_obj.show_details()
employee_obj.show_details()
partime_obj.show_details()
consultant_obj.show_details()
