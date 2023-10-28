class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0
        "this allows us to modify the value of speed directly when making an instance"

    def describe(self):
        dis_car = self.make.title() + " " + self.model.title() + " " + str(self.year)
        return dis_car
    def spd(self):
        print(f" moving at {str(self.speed)}  km/hr")



mycar = Car("titan", "nissan", 2009)
print(mycar.describe())
mycar.spd()
mycar.speed = 26
mycar.spd()
