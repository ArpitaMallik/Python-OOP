class Animal:
    def __init__(self):
        self.name = "Toby"

    def speak(self):
        print(f"{self.name} makes a sound.")

class Cat(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed
    
    def speak(self):
        super().speak()
        print(f"{self.name} meows. He is a {self.breed} cat.")

cat = Cat("Persian")
cat.speak()