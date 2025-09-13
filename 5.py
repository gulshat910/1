numbers = [12,-5,23,0,4,17,-8,0,11]
print(f"Количество элементов в списке {len(numbers)}")
print(f"Последний элемент списка: {numbers[-1]}")
reversed_numbers = numbers[::-1 ]
print(f"Список в обратном порядке {reversed_numbers}")
if 5 in numbers and 17 in numbers:
    print("Да")
else:
    print("Нет")
