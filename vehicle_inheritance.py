class Vehicle:
    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


# Create object of Car
car = Car()

# Call both methods
car.start()
car.drive()