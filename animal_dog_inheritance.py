# Parent class
class Animal:
    def eat(self):
        print("Animal is eating")


# Child class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")


# Create object of Dog
dog = Dog()

# Call both methods
dog.eat()   # Inherited from Animal
dog.bark()  # Defined in Dog