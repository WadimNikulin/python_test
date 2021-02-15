from sys import argv
from itertools import cycle

script_1 = argv
my_list = [5, 2, 2, 4, 5, 9, 7, 8, 9, 10]
m = 0
for n in cycle(my_list):
    if m > 10:
        break
    else:
        print(n)
        m += 1
