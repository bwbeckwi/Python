class dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight


    def bark(self):
        print("Woof Woof! My name is: {}, I weigh {} pounds and I am {} years old".format(self.name, str(self.weight), str(self.age)))


    def walk(self, distance):
        print("{} just walked a distance of: {}".format(self.name,str(distance)))


mydog = dog("Sam", 5, 68)

mydog.walk(distance="1 mile")