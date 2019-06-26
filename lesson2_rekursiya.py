'''
1. Написать рекурсивную функцию, которая возвращает сумму цифр числа
2. Дано натуральное число N. Выведите слово YES, если число N является точной
   степенью двойки, или слово NO в противном случае.
3. Дано натуральное число N. Выведите все его цифры по одной, в обратном
   порядке, разделяя их пробелами или новыми строками.1/5
'''


def get_sum_digit_of_numeric(num):
    if len(num) == 1:
        return num[0]
    return int(num[len(num)-1]) + int(
        get_sum_digit_of_numeric(num[:len(num)-1]))


def check_digit(num):
    if num == 2:
        return 'Yes'
    elif not num % 2:
        return check_digit(num / 2)
    return 'No'


def rollback(dig, num):
    if num == 0:
        print(dig[0])
        return
    print(dig[num], end=' ')
    rollback(dig, num - 1)


if __name__ == "__main__":
    # 1
    input_user = input('input a numeric: ')
    while not input_user.isdigit():
        input_user = input("Wrong data. Try again: ")
    print(get_sum_digit_of_numeric(input_user))
    # 2
    print(check_digit(int(input("input a numeric"))))
    # 3
    string = input('Input a numeric')
    rollback(string, len(string) - 1)
