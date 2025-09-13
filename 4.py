start = int(input("Введите число: "))
end = int(input("Введите число: "))
found = False
for num in range( start ,end + 1):
    if num % 2 == 0:
        print(num, end="")
        found = True
if not found:
    print("В этом диапазоне нет четных чисел")
