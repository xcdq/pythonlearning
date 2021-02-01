class Car():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name, self.age)

    def printtt(self):
        print(self.name, self.age)


class ElectricCar(Car):
    def __init__(self, name, age):
        super().__init__(name, age)
        print(self.name, self.age)
        print("__________!!!!!___________")


ccc = ElectricCar("ccc", 23)
