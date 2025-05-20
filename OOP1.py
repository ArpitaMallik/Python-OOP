class employee:
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.designation = "Software Engineer"

    def travel(self, destination):
        print(f"Sam is traveling to {destination}")

#create an object of the class
sam = employee()

#accessing the attributes of the class
print(sam.designation)

#calling a method of the class
sam.travel("Dhaka")