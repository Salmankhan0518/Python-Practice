marks = int(input("Enter your marks: "))

if marks >= 101:
    print("Please verify your marks")
    exit()

if marks >= 90 and marks <= 100:
    print("Your Grade is A")
elif marks >= 80 and marks <= 89:
    print("Your Grade is B")
elif marks >= 70 and marks <= 79:
    print("Your Grade is C")
elif marks >= 60 and marks <= 69:
    print("Your Grade is D")
else:
    print("Fail")                