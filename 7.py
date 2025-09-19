import math

def calculate_circle_area(radius):
    return math.pi * radius * radius

def is_positive(number):
    if number > 0:
        return True
    else:
        return False

# Демонстрация работы функций
r = 3
print("Площадь круга с радиусом", r, "равна", calculate_circle_area(r))

num = -2
print(num, "положительное?", is_positive(num))

num = 4
print(num, "положительное?", is_positive(num))
