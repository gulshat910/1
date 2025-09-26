import random

numbers = []
for i in range(15):
    numbers.append(random.randint(-10, 10))

positives = []
for n in numbers:
    if n > 0:
        positives.append(n)

squares = []
for n in numbers:
    squares.append(n * n)

print("Исходный список:", numbers)
print("Положительные числа:", positives)
print("Квадраты чисел:", squares)
