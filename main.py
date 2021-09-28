import random
import numpy as nd

data = []

for i in range(1,11):
    row = []
    for j in range(1,6):
        rand_num = random.randint(1,10)
        row.append(rand_num)
    data.append(row)

for row in data:
    for value in row:
        print(value, end="\t")
    print()

smallest_num = largest_num = data[0][0]
for row in data:
    if min(row) < smallest_num:
        smallest_num = min(row)
    if max(row) > largest_num:
        largest_num = max(row)
print("smallest:", smallest_num, "largest:", largest_num)

user_num = int(input("Please enter a number between [1,10] to count:"))
count = 0
for row in data:
    for num in row:
        if num == user_num:
            count += 1
print("count:", count)

user_num = int(input("Please enter a number between [1,10] to remove:"))
found = False
for row in data:
    while user_num in row:
        found = True
        row.remove(user_num)
if found:
    print(data)
else:
    print("Sorry your number is not here")