'''
1. Написать функцию, которая вычисляет среднее арифметическое элементов
   массива(списка), переданного ей в качестве аргумента.
2. Дан одномерный массив, состоящий из натуральных чисел. Выполнить сортировку
   данного массива по возрастанию суммы цифр чисел. Например, дан массив чисел
   [14, 30, 103]. После сортировки он будет таким: [30, 103, 14],
   так как сумма цифр числа 30 составляет 3, числа 103 равна 4, числа 14
   равна 5.Вывести на экран исходный массив, отсортированный массив, а также для
   контроля сумму цифр каждого числа отсортированного массива.
   Написать 2 функции:
   а) функция, которая возвращает сумму цифр
   б) функция, которая сортирует массив
3. Написать функцию, которая заполняет массив случайными числами в диапазоне,
   указанном пользователем. Функция должна принимать два аргумента - начало
   диапазона и его конец, при этом ничего не возвращать. Вывод значений
   элементов массива должен происходить в основной ветке программы.
'''

import random


def get_avarage(list_in):
    list_digits = list_in.split(",")
    sum_digit = 0
    for digit in list_digits:
        print(digit)
        sum_digit = sum_digit + int(digit)
    return sum_digit / len(list_digits)


def get_sum_digit(digit):
    st = str(digit)
    sum_d = 0
    for i in st:
        sum_d += int(i)
    return sum_d


def sort_shell(array):
    sorted_sums = []
    half_len = int(len(array)/2)
    while half_len > 0:
        for i in range(len(array) - half_len):
            j = i
            while j >= 0 and array[j] > array[j + half_len]:
                array[j], array[j + half_len] = array[j + half_len], array[j]
                j -= 1
        half_len = int(half_len / 2)
    for element_of_array in array:
        sorted_sums.append(get_sum_digit(element_of_array))
    return array, sorted_sums


def find_random(min_digit, max_digit):
    array_of_range.append(random.randint(int(min_digit), int(max_digit)))


def check_input_digit(string):
    user_digit = input(string)
    while not user_digit.isdigit():
        user_digit = input("Wrong data. Try again: ")
    return int(user_digit)


if __name__ == "__main__":
# 1
    print(get_avarage(input('Input string of digit separated by ,')))
# 2
    array_of_input = [12, 601, 43, 67, 101, 34, 1]
    print(array_of_input)
    array_of_input, sort_sum = sort_shell(array_of_input)
    print(array_of_input)
    print(sort_sum)
# 3
    array_of_range = []
    count_of_element = check_input_digit('input range of list: ')
    min_input = check_input_digit('Input min: ')
    max_input = check_input_digit('Input max: ')
    while max_input < min_input:
        print('Max should be more then Min. Input new Max')
        max_input = check_input_digit('Input max: ')
    for counter in range(int(count_of_element)):
        find_random(min_input, max_input)
    print(array_of_range)
