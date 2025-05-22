class Parent():
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"{self.name} is my name.")\
        
class Child1(Parent):
    def play(self):
        print(f"{self.name} plays with toys.")

class Child2(Parent):
    def study(self):
        print(f"{self.name} studies hard.")


child1 = Child1("Arpi")
child2 = Child2("Saumik")

child1.greet()
child1.play()

child2.greet()
child2.study()
child2.play()  # This will raise an error because Child2 does not have the play method