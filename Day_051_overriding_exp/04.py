'''
Assignment 4:

Create a parent class Vehicle with a method speed() that prints "Speed varies for different vehicles."

Create subclasses:

Car that overrides speed() to print "The car speed is 120 km/h."

Bike that overrides speed() to print "The bike speed is 80 km/h."

Use polymorphism to display the speed of different vehicles in the Main class.
'''

class Vehicle:
    def speed(self):
        print("Speed varies for different vehicles.") 

class Car(Vehicle):
    def speed(self):
        print("The car speed is 120 km/h.")

class Bike(Vehicle):
    def speed(self):
        print("The bike speed is 80 km/h.") 


class Main:

   def start(self):
       speeds = [Vehicle(), Car(), Bike()]
 
       for i in speeds:
           i.speed() 

run = Main()
run.start()

    