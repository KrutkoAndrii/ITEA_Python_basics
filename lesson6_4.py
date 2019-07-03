'''
    Реалізувати функцію, що буде імпорnувати метод з файла test2.py і
    передавати в нього список, який буде формуватись за наступним алгоритмом:
    кожен елемент складає з себе середнє арифметичне кожного рядку файла
    test3_result.txt. Тобто 100 елементний список.
'''
import pickle



if __name__ == "__main__":
    with open('test2.txt', 'rb') as file_def:
        function_from_file = pickle.load(file_def)
        print(function_from_file)
        arrays_of_digits = [2, 3, 4]
        print(eval(function_from_file))
       # print(function_from_file([2,3,4]))
        #exec(function_from_file)
