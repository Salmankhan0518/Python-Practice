def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="Salman", power="XYZ")
print_kwargs(name="Salman", power="XYZ", enemy="ABC")