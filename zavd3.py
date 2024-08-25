while True:
    try:
        N = int(input("Введіть ціле число N (1 < N < 9): "))

        if 1 < N < 9:
            for i in range(N):
                for j in range(N, i, -1):
                    print(j, end=" ")
                print()
        else:
            print("Помилка: Число повинно бути в межах від 2 до 8.")
    except ValueError:
        print("Помилка: Будь ласка, введіть ціле число.")

    repeat = input("Бажаєте повторити? (y/n): ").strip().lower()
    if repeat != 'y':
        break