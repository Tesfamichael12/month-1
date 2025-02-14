class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.__num_doors = num_doors

    def describe(self):
        return f"Car: {self.make} {self.model}, Doors: {self.__num_doors}"


class Bike(Vehicle):
    def __init__(self, make, model, bike_type):
        super().__init__(make, model)
        self.__bike_type = bike_type

    def describe(self):
        return f"Bike: {self.make} {self.model}, Type: {self.__bike_type}"
    
    if __name__ == "__main__":
        car = Car("Toyota", "Corolla", 4)
        bike = Bike("Yamaha", "MT-07", "Sport")
    
        print(car.describe())
        print(bike.describe())
