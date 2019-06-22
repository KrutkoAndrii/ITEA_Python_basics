# Проверить является ли введенное число простым.
# Число считается простым если оно не делится
# нацело на все числа до квадратного корня этого числа
import math

if __name__ == "__main__":
    user_digit = input("Input a numeric: ")
    while not user_digit.isdigit():
        user_digit = input("Wrong data. Try again: ")
    user_digit = int(user_digit)
    sq_digit = round(math.sqrt(user_digit))
    for i in range(2, sq_digit):
        if not (user_digit % i):
            print("Not Simple!")
            break
    else:
        print("Simple!")
