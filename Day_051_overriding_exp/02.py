'''

2.

Create a parent class Animal with a method makeSound() that prints "Some generic sound."

Create subclasses:

Dog that overrides makeSound() to print "Woof Woof."

Cat that overrides makeSound() to print "Meow Meow."

In the Main class, use polymorphism to call makeSound() on different Animal objects.

'''

class Animal:
    def makeSound(self):
        print("Some generic sound.")

class Dog(Animal):
    def makeSound(self):
        print("Woof Woof.")

class Cat(Animal):
    def makeSound(self):
        print("Meow Meow.")


class  Main:
    def start(self):
       sounds = [Animal(), Dog(), Cat()]

       for i in sounds:
           i.makeSound()

run = Main()
run.start()


     