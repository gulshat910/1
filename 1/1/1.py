# создаём файл с учениками
f = open("students.txt", "w", encoding="utf-8")
f.write("Иванов;101;5,4,5\n")
f.write("Петров;101;3,4,4\n")
f.write("Сидоров;102;5,5,5\n")
f.write("Анна;102;4,5,5\n")
f.write("Ольга;101;2,3,3\n")
f.close()

# читаем файл
f = open("students.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

students = []
for line in lines:
    parts = line.strip().split(";")
    name = parts[0]
    group = parts[1]
    grades = parts[2].split(",")
    grades = [int(x) for x in grades]
    students.append([name, group, grades])

# ищем отличников
f = open("excellent_students.txt", "w", encoding="utf-8")
for s in students:
    if all(g == 5 for g in s[2]):
        f.write(s[0] + " (" + s[1] + ")\n")
f.close()

# средний балл по группам
groups = {}
for s in students:
    if s[1] not in groups:
        groups[s[1]] = []
    groups[s[1]].extend(s[2])

for g in groups:
    avg = sum(groups[g]) / len(groups[g])
    print("Группа", g, "средний балл:", avg)
