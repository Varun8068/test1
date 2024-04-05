# Base class (Superclass)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

# Derived class (Subclass) inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Derived class (Subclass) inheriting from Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Creating instances of the derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling the speak method on instances
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
