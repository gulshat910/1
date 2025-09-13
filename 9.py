import  random
numbers = [random.randint(-10,10) for _ in  range(15)]
print("Исходный список:", numbers)
positive_numbers = [num for num in numbers if num > 0]
print("Положительные числа:", positive_numbers)
