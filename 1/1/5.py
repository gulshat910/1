import math

# --- Объявляем функцию ---
def safe_apply(func, data):
    results = []
    errors = []
    for x in data:
        try:
            results.append(func(x))
        except Exception as e:
            errors.append((x, type(e).__name__))
    return results, errors


# --- Демонстрация работы ---
data = ['4', '16', 'text', '-25', '9.0']

# лямбда-функция для вычисления квадратного корня
sqrt_func = lambda x: math.sqrt(float(x))

# вызов функции
results, errors = safe_apply(sqrt_func, data)

print("✅ Результаты:", results)
print("⚠️ Ошибки:", errors)
