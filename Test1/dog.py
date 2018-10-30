class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof Woof! My name is: " + self.name)

    def walk(self, distance):
        print("I just walked a distance of: " + str(distance))
