# Найти факториал числа


def get_factorial(digit_base):
    if digit_base == 0:
        return 1
    else:
        return digit_base * factorial(digit_base - 1)


if __name__ == "__main__":

    user_input = input("Enter a numeric for factorial ")
    while not user_input.isdigit():
        user_input = input("Wrong data. Try again: ")
    user_input = int(user_input)
    print(get_factorial(user_input))
