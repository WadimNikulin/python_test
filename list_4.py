my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = []
n = len(my_list)

print(my_list)

for el in my_list:
    if my_list.count(my_list[len(my_list) - n]) == 1:
        new_list.append(my_list[len(my_list) - n])
        n -= 1
    else:
        n -= 1

print(new_list)
