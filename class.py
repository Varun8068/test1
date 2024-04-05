class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"The {self.make} {self.model} is now being driven.")


# Creating an object of the Car class
my_car = Car("Toyota", "Corolla")

# Accessing attributes and calling methods of the object
print(f"My car is a {my_car.make} {my_car.model}.")
my_car.drive()









class Car:
    # Class attribute
    category = "Vehicle"

    # Constructor method (initialize object)
    def __init__(self, make, model, year):
        # Instance attributes
        self.make = make
        self.model = model
        self.year = year

    # Method to get the car's age
    def age(self, current_year):
        return current_year - self.year

    # Method to display information about the car
    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

# Creating instances of the Car class
car1 = Car("Toyota", "Corolla", 2015)
car2 = Car("Ford", "Mustang", 2020)

# Accessing attributes and calling methods of the instances
car1.display_info()
print(f"{car2.make} {car2.model} is {car2.age(2024)} years old.")

