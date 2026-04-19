password = input("Enter password i'll let you is weak or not: ")

if len(password) < 6:
    print("is a Weak password")
elif len(password) >= 6 and len(password) < 10:
    print("is a Medium strong password")
elif len(password) > 10:
    print("is a Strong password") 