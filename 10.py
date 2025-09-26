while True:
    user_input = input("Введите число или 'стоп': ")
    
    if user_input.lower() == "стоп":
        print("Программа завершена.")
        break

    try:
        number = float(user_input)
        print("Вы ввели число:", number)
    except ValueError:
        print("Ошибка: введите число или 'стоп'.")
