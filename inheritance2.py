class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return f"{self.name} will bark like bau bau"
class Cat(Animal):
    def speak(self):
        return f"{self.name} will speak like meow meow"
dog=Dog("buddy")
cat=Cat("bab")
print(dog.speak())
print(cat.speak())


