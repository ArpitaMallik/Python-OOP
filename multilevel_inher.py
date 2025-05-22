class Grandparent():
    def __init__(self, name):
        self.name = name

    def tell_story(self):
        print(f"{self.name} tells a story.")

class Parent(Grandparent):
    def work(self):
        print(f"{self.name} goes to work.")
        
class Child(Parent):
    def play(self):
        print(f"{self.name} plays with toys.")

child = Child("Arpi")
child.tell_story()
child.work()
child.play()