import math

# данные
data = ["4", "16", "text", "-25", "9.0"]

results = []
errors = []

for x in data:
    try:
        # пробуем вычислить квадратный корень
        results.append(math.sqrt(float(x)))
    except:
        # если ошибка, записываем элемент и тип ошибки
        errors.append(x)

print("Результаты:", results)
print("Ошибки:", errors)
