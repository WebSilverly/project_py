class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def describe(self):
        print(f'Dog name:{self.name.title()}\nDog age:{self.age}')

lan = Dog('jag', 2)
lan.describe()



