'''
Assignment 5:

Create a parent class Employee with a method calculateSalary() that prints "Base salary calculation for Employee."

Create subclasses:

Manager that overrides calculateSalary() to add a bonus to the base salary.

Developer that overrides calculateSalary() to calculate salary based on hours worked.

Demonstrate the overridden method in the Main class by creating an array of Employee objects and calling calculateSalary() on each.
'''

class Employee:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def calculateSalary(self):
        print("Base salary calculation for Employee.")

class Manager(Employee):
    def __init__(self, base_salary, bonus):
       super().__init__(base_salary)
       self.bonus = bonus 
    
    def calculateSalary(self):
       salary = self.base_salary + self.bonus
       print(salary)


class Developer(Employee):
   def __init__(self, base_salary, hours):
       super().__init__(base_salary)
       
       self.hours = hours

   def calculateSalary(self):
       salary = self.base_salary + self.hours
       print(salary)


class Main:
    def start(self):
        salaries = [Employee(int(input("base salary: "))), Manager(int(input("base salary: ")), int(input("bonus: "))), Developer(int(input("base salary: ")), int(input("hours: ")))]

        for i in salaries:
            i.calculateSalary()

run = Main()
run.start()

        
