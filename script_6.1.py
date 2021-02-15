from sys import argv
from itertools import count

script_1, numbers = argv
for n in count(int(numbers)):
    if n > 10:
        break
    else:
        print(n)

