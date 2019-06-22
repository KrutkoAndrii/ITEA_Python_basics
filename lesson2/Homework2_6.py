# Нарисовать равнобедренный треугольник из символов ^. Высоту выбирает пользователь.
if __name__ == "__main__":
    user_digit = input("Input a numeric: ")
    while not user_digit.isdigit():
        user_digit = input("Wrong data. Try again: ")
    user_digit = int(user_digit)
    for i in range(user_digit):
        print(" "*(user_digit - i + 1) + "^"*(1 + i * 2))
