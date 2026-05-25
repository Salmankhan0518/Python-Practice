class Car:
    total_car = 0
    def __init__(self, brand = "Honda", model = "Cevic"):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def set_brand(self, new_brand):
        if isinstance(new_brand, str) and new_brand.strip() != "":
            self.__brand = new_brand
        else:
            print("Error: Inva;id brand name!") 

    def fuel_type(self):
        return "Fuel type is Deisel or Petrol"           

        
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    @staticmethod
    def car_description():
        return "Cars are means of transpotation"
    
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

    def fuel_type(self):
        return "Fuel type is Electrical Charge"    


my_tesla = ElectricCar("Tesla", "Model S", "85KWH")
safari = Car("Tata", "Safari")
my_car = Car("Test", "Test")
my_car.model = "City"

# print(my_tesla.__brand)
# my_tesla.set_brand("Honda")

print(my_tesla.fuel_type())
print(safari.fuel_type())
print(Car.total_car)

print(my_car.model)


# print(my_car.car_description())
print(Car.car_description())



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