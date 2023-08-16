import random

numbers = []

#Picks 5 random numbers between 1-99

while True:
    if len(numbers) == 5:
        break
    pick = random.randint(1, 99)
    if pick not in numbers:
        numbers.append(pick)

numbers.sort()
print("The Lottery numbers are: ", numbers)

for i in numbers:
    print(i, end= ' ')



