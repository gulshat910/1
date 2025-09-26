import numpy as np

# создаём две матрицы 5x5
A = np.random.randint(1, 11, (5, 5))
B = np.random.randint(1, 11, (5, 5))

print("A:\n", A)
print("B:\n", B)

# поэлементное произведение
print("A*B:\n", A * B)

# матричное произведение
print("A@B:\n", A @ B)

# определитель
print("det(A):", np.linalg.det(A))

# транспонированная B
print("B.T:\n", B.T)

# обратная матрица (если можно)
if np.linalg.det(A) != 0:
    print("inv(A):\n", np.linalg.inv(A))
else:
    print("Обратной матрицы нет")

# решаем систему A*x = C, где C = сумма строк A
C = A.sum(axis=1)
if np.linalg.det(A) != 0:
    x = np.linalg.solve(A, C)
    print("Решение A*x=C:\n", x)
else:
    print("Система не имеет решения")
