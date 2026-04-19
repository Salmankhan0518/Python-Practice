orderSize = input("Enter Coffee size in /Medium/Large/Small: ")
extraShot = input("You want Extra shot or not enter with Yes/No: ")
extraShot = extraShot.lower()

if extraShot == "yes":
    extraShot = True
else:
    extraShot = False

if extraShot:
    print(orderSize + " Coffee with an Extra Shot")
else:
    print(orderSize + " Coffee")         