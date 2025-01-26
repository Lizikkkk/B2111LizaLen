class Student:
    def __init__(self, name):
        self.name = name
        self.height = 152
        print("Hello!")

maxim = Student("Maxim")
print(maxim.height)
print(maxim.name)