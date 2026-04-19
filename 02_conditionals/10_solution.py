animalSpecies = input("Enter Animal Species Cat or Dog: ")
animalSpecies = animalSpecies.lower()
age = int(input("Enter the Age of yhe Animal: "))

if animalSpecies == "dog" and age < 2:
    print("Puppy food")
elif animalSpecies == "cat" and age > 5:
    print("Senior cat food")
else:
    print("Enter valid credentials")    