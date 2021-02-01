class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title()+" is now sitting.")

    def roll(self):
        print(self.name.title()+" is rolled over")


d = Dog(name="aaa", age='12')
d.sit()
d.roll()
