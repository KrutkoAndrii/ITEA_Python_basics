'''
1. Вывести квадраты всех чисел от 1 до 10
2. Выводить квадраты чисел до тех пор пока они меньше 1000.
3. Извлекать квадратный корень из введенного пользователем числа до тех пор,
   пока значение больше 10.
4. Вывести все заглавные буквы в строке
5. Напишите программу, которая выводит сумму введенных пользователем чисел.
   Числа вводятся одной строкой.
6. Напишите программу используя цикл с предусловием while для вывода каждого
   четного положительного числа от 0 до 20.
7. Организовать непрерывный ввод цифр с клавиатуры, пока пользователь НЕ
   введёт 0 После ввода нуля, показать на экран количество чисел, которые были
   Введены, их общую сумму и среднее арифметическое.
8. Найти сумму цифр числа 2 способами: циклом интерпретируя число как str и с
   помощью операций ‘%’, ‘/’, интерпретируя число как Integer
9. Вывести n чисел фибоначчи: 1 1 2 3 5 8 13...
'''

import math


if __name__ == "__main__":
# 1
    for i in range(11):
        print(i ** 2)
# 2
    i = 0
    while True:
        i += 1
        if i**2 > 1000:
            break
        else:
            print(i**2)
# 3
    my_string = input('input a numeric ')
    n = math.sqrt(int(my_string))
    while n > 10:
        print(n)
        n = math.sqrt(n)
# 4
    print('Task 4')
    st = input('input a string ')
    for i in st:
        if i.isupper():
            print(i, end='')
# 5
    print('Task 5')
    st = input('input line of numeric separated by ,')
    st_digit = st.split(',')
    sum_all = 0
    for st_dig in st_digit:
        if st_dig.isdigit():
            sum_all += int(st_dig)
    print(sum_all)
# 6
    print('Task 6')
    flag = 0
    i = 0
    while i < 20:
        if flag == 4:
            print(i, end=' ')
            fl = 0
        i += 1
        flag += 1
# 7
    print('Task 7')
    dg_count = 0
    dg_sum = 0
    st = '1'
    while int(st) != 0:
        st = input('input a numeric ')
        if st.isdigit():
            dg_count += 1
            dg_sum += int(st)
        else:
            st = '0'
    if dg_count != 0:
        print('count:'+str(dg_count) + ' sum: '+str(dg_sum) + ' avr '+str(
               dg_sum / dg_count))
# 9
    print('Task 9')
    count = input("Input a numeric ")
    fibonachi_f = 0
    fibonachi_s = 1
    print('1')
    for i in range(int(count) - 1):
        fibonachi = fibonachi_f+fibonachi_s
        print(fibonachi, end=' ')
        fibonachi_f = fibonachi_s
        fibonachi_s = fibonachi
