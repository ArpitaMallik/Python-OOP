class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self):
        self.behaviour = "friendly"      
    def speak(self):
        print(f"{self.name} barks. He is very {self.behaviour}.")


# animal = Animal("Generic Animal")
# animal.speak()

dog = Dog("Toby")
dog.speak()
# dog.speak1()