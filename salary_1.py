from sys import argv

salary, total_hours, rate, prize = argv
salary1 = (int(total_hours) * int(rate)) + int(prize)

print(salary1)
