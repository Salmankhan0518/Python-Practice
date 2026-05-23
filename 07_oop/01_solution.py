class Car:
    def __init__(self, brand = "Honda", model = "Cevic"):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}" 

class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize


my_tesla = ElectricCar("Tesla", "Model S", "85KWH")
print(my_tesla.full_name())



# my_car = Car("Toyota", "Carolla")

# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata", "Safari")

# print(my_new_car.brand)
# print(my_new_car.model)

# my_other_car = Car()

# print(my_other_car.brand)
# print(my_other_car.model)