class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
    @staticmethod
    def from_string(string):
        split_list = string.split('-')
        firstname, lastname, salary = split_list
        return Employee(firstname, lastname, salary)


emp2 = Employee.from_string("John-Smith-55000")
print(emp2.firstname)
print(emp2.lastname)
print(emp2.salary)