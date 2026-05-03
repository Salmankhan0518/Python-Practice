# def even_number_generator(number):
#     for i in range(2, number+1):
#         if i % 2 == 0:
#             print("These are EVEN number: ", i)

# even_number_generator(10)

def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield i

for num in even_generator(10):
    print(num)



