import math

def circleStats(radius):
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = circleStats(3)

# a = a.__floor__()
# c = c.__floor__()

print("Area: ", round(a, 2), "Circumference: ", round(c), 2)