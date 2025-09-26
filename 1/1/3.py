import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# создаём данные
data = {
    "Товар": ["Яблоко", "Банан", "Апельсин", "Яблоко", "Банан"],
    "Цена": [50, np.nan, 60, 55, 20000],   # есть NaN и выброс
    "Количество": [10, 5, 7, -3, 20]       # есть выбросы
}

df = pd.DataFrame(data)

# заменяем NaN медианой
median_price = df["Цена"].median()
df["Цена"] = df["Цена"].fillna(median_price)

# убираем выбросы по количеству
df = df[(df["Количество"] >= 1) & (df["Количество"] <= 1000)]

# создаём колонку с общей стоимостью
df["Общая_стоимость"] = df["Цена"] * df["Количество"]

# группируем по товару и считаем суммарную выручку
revenue = df.groupby("Товар")["Общая_стоимость"].sum()

print("Выручка по товарам:\n", revenue)

# строим график
revenue.plot(kind="bar")
plt.ylabel("Сумма")
plt.title("Выручка по товарам")
plt.show()
