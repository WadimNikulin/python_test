import random

my_list = []
n = 0
while n < 10:
    a = random.randint(0, 200)
    my_list.append(a)
    n += 1

print(my_list)

new_list = []
m = len(my_list)-1

while m >= 1 and m < len(my_list):
    el = my_list[len(my_list)-n]
    if el < my_list[len(my_list)-m]:
        new_list.append(my_list[len(my_list)-m])
        m -= 1
        n -= 1
    else:
        m -= 1
        n -= 1

print(new_list)