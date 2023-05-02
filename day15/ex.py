import random

lower = ""
upper = ""
while not lower or not upper:
    try:
        lower = int(input("Enter the lower bound: "))
        upper = int(input("Enter the upper bound: "))
    except ValueError:
        continue
    print(random.randint(lower, upper))