from functools import reduce

my_list = []


def func(a, b):
    return a * b


for n in range(100, 1002, 2):
    my_list.append(n)
print(my_list)

result = reduce(func, my_list)
print(result)
