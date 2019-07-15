'''
    Реалізувати функцію, що буде імпорnувати метод з файла test2.py і
    передавати в нього список, який буде формуватись за наступним алгоритмом:
    кожен елемент складає з себе середнє арифметичне кожного рядку файла
    test3_result.txt. Тобто 100 елементний список.
'''
from test2 import count_degree


def make_result():
    ''' count array from file '''
    array_of_averages = []
    with open('test3_result.txt', 'r') as file_data:
        for sting_from_file in file_data:
            array_from_strings = [int(s) for s in
                                  sting_from_file[:-1].rsplit(' ')]
            array_of_averages.append(sum(array_from_strings) /
                                     len(array_from_strings))
    file_data.close()
    return array_of_averages


if __name__ == "__main__":
    array_of_digits = make_result()
    print(count_degree(array_of_digits))
