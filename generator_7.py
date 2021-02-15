import math


def fact(n):
    for i in range(1, n + 1):
        yield (math.factorial(i))


f = fact(6)
print(f)

for n in f:
    print(n)
