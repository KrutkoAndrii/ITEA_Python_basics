# Вывести сумму всех делителей заданного числа

if __name__ == "__main__":
    user_digit = input("Input a numeric: ")
    while not user_digit.isdigit():
        user_digit = input("Wrong data. Try again: ")
    user_digit = int(user_digit)
    div_sum = 1
    for i in range(2, user_digit+1):
        if not (user_digit % i):
            div_sum += i
    print("Result is: " + str(div_sum))
