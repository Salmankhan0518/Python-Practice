distance = int(input("Enter the Distance in Km: "))

if distance <= 3:
    print("Walk")
elif distance > 3 and distance <= 15:
    print("Bike")
elif distance > 15:
    print("Car")
else:
    print("Enter valid distance")