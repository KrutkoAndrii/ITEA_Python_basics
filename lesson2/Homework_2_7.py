# Напишите программу “угадай число”.  Компьютер генерирует рандомное число (функция random),
# пользователь вводит числа, пока не угадает, а компьютер отвечает больше или меньше

import random

if __name__ == "__main__":

    user_digit = input("Input a numeric: ")
    while not user_digit.isdigit():
        user_digit = input("Wrong data. Try again: ")
    user_digit = int(user_digit)
    random_user = random.randint(0, user_digit)
    print(random_user)  # для проверки работоспособности
    while True:
        user_digit = input("Input your answer: ")
        while not user_digit.isdigit():
            user_digit = input("Wrong data. Try again: ")
        user_digit = int(user_digit)
        if random_user > user_digit:
            print('More')
        elif random_user < user_digit:
            print("Less")
        else:
            print("Сongratulations you win!")
            break
