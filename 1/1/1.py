# Создаём класс Student
class Student:
    def __init__(self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def is_excellent(self):
        return self.average_grade() >= 4.5


#Создаём файл со студентами
with open("students.txt", "w", encoding="utf-8") as f:
    f.write("Иванов;101;5,4,5\n")
    f.write("Петров;101;3,4,4\n")
    f.write("Сидоров;102;5,5,5\n")
    f.write("Анна;102;4,5,5\n")
    f.write("Ольга;101;2,3,3\n")

#Читаем файл и создаём список объектов
students = []
with open("students.txt", "r", encoding="utf-8") as f:
    for line in f:
        name, group, grades_str = line.strip().split(";")
        grades = list(map(int, grades_str.split(",")))
        students.append(Student(name, group, grades))

#Записываем отличников
with open("excellent_students.txt", "w", encoding="utf-8") as f:
    for s in students:
        if s.is_excellent():
            f.write(f"{s.name} ({s.group})\n")

#Средний балл по группам
groups = {}
for s in students:
    if s.group not in groups:
        groups[s.group] = []
    groups[s.group].extend(s.grades)

for group, grades in groups.items():
    avg = sum(grades) / len(grades)
    print(f"Группа {group}, средний балл: {avg:.2f}")
