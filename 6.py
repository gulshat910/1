student = {
    "name": "Иван",
    "age": 19,
    "course": "Программирование",
    "grades": [4,5,3,5,4]
}
print("Имя:", student["name"])
print("Курс:", student["course"])
average = sum(student["grades"]) / len(student["grades"])
print("Средний балл:", average)
student["grades"].append(5)
print("Обновленный словарь:", student)
