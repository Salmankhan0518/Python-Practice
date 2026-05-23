class Car:
    def __init__(self, brand = "Honda", model = "Cevic"):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !"

    def set_brand(self, new_brand):
        if isinstance(new_brand, str) and new_brand.strip() != "":
            self.__brand = new_brand
        else:
            print("Error: Inva;id brand name!")    

        

    def full_name(self):
        return f"{self.__brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize


my_tesla = ElectricCar("Tesla", "Model S", "85KWH")
# print(my_tesla.__brand)
my_tesla.set_brand("Honda")
print(my_tesla.get_brand())



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