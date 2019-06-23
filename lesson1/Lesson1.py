'''
1. Посчитайте значение выражения:3^128*2^128
2. Выведете слово python 100 раз
3. Напишите программу, которая считает сколько букв ‘o’ в заданной строке
4. Напишите программу, которая сортирует заданный список из чисел
5. Напишите программу, которая считает сумму последних цифр двух введенных
   пользователем чисел
6. Напишите программу, которая переводит температуру в Кельвинах в Цельсии
7. Напишите программу, которая преобразует строку, в которой записаны слова
   через “,” в список из этих слов
'''

if __name__ == "__main__":
# 1
    print("Задание №1")
    print(3 ** 128 * 2 ** 128)
# 2
    print("Задание №21")
    print('Python'*100)
# 3
    print("Задание №3")
    str = 'molokovoz'
    print(str.count('o'))
# 4
    print("Задание №4")
    str = '2,5,1,34,7'
    my_lists = str.split(",")
    my_lists2 = []
    i = 0
    m = (len(my_lists))
    while i <= m-1:
        my_lists2.append(int(my_lists[i]))
        i += 1
    my_lists2.sort()
    print(my_lists2)
# or
    my_lists3 = [2, 4, 1, 22, 6, 10]
    my_lists3.sort()
    print(my_lists3)
# 5
    print("Задание №5")
    print('input a numeric №1')
    my_str51 = input()
    if my_str51.isdigit():
        n51 = int(my_str51[len(my_str51)-1])
    else:
        print("Error incoming data ")
        n51 = 0
    print('imput a numeric №2')
    my_str52 = input()
    if my_str52.isdigit():
        n52 = int(my_str52[len(my_str52)-1])
    else:
        print("Error incoming data ")
        n52 = 0
    print(n51 + n52)
# 6
    print("Задание №6")
    print("input T(kelvin)")
    Kelvin = input()
    print(int(Kelvin)-273)
# 7
    print("Задание №7")
    print("Input a string with ','")
    str7 = input()
    my_lists7 = str7.split(",")
    print(my_lists7)
