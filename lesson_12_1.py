class Vehicle:

    def drive(self):
        return "your vehicle can drive"


class Car(Vehicle):
    wheels = 4  # атрибут класу
    seats = 4  # атрибут класу
    windows = 4  # атрибут класу
    count_cars = 0

    def __init__(self, make: str, model: str, fuel: str):
        self.make = make.upper()
        self.model = model.lower()
        self.fuel = fuel.capitalize()
        self.doors = 5
        Car.count_cars += 1

    def start_engine(self, men_count: int):
        return f"{self.make} {self.model} engine started with {men_count} people"

    @staticmethod
    def add_number(number: int):
        return number ** 3

    @classmethod
    def change_wheels(cls):
        cls.wheels += 1
        cls.seats += 1
        cls.windows += 1

    @classmethod
    def how_many_cars(cls, type_of_cars: str):
        return f"you created {cls.count_cars} {type_of_cars} cars"


tesla_car = Car("tesla", "rodster", "petrol")
ford_car = Car("ford", "bronco", "diesel")
bmw_car = Car(make="bmw", fuel="diesel", model="bronco")

tesla_car.color = "red"
tesla_car.model = "model 3"

Car.change_wheels()

print(tesla_car.start_engine(5))
print(tesla_car.color)
print(tesla_car.wheels)

print(ford_car.start_engine(7))
print(bmw_car.start_engine(9))
print(bmw_car.start_engine(9))
print(bmw_car.drive())

print(bmw_car.add_number(5))
print(Car.how_many_cars("sedan"))




