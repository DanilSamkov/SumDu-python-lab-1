while True:
    try:
        a = float(input("Введіть значення a (додатнє число): "))
        b = float(input("Введіть значення b (додатнє число): "))

        # Перевірка, чи є a та b додатніми
        if a <= 0 or b <= 0:
            print("Помилка: числа a та b повинні бути додатніми.")
        else:
            # Обчислення X
            if a < b:
                X = a / b + 1
            elif a == b:
                X = -1
            else:
                X = (a * b - 5) / a

            print(f"Значення X: {X}")

    except ValueError:
        print("Помилка: введіть числове значення.")

    # Запит на продовження чи завершення роботи програми
    choice = input("Бажаєте повторити? (y/n): ").strip().lower()
    if choice != 'y':
        break