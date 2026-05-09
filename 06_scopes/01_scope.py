username = "salmankhan"

def func():
    # username = "XYZ"
    print(username)

print(username)    
func()

x = 99

# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)

def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
g = chaicoder(3)

print(f(3))
print(g(3))