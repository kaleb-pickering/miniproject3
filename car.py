class Car:
    def __init__(self, make, model, year =1):
        self.make = make
        self.model = model
        self.year = year

my_car, new_car, new_car2 = Car('Nissian', 'Pathfinder', 2005), Car('Ford', 'F-150', 2015), Car('Kia', 'Sorento', 2022)

cars =  [my_car, new_car, new_car2]

for car in cars:
    print(f'{car.make} {car.model} {car.year}  ')