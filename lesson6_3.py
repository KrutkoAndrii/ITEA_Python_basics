'''
   Створити функцію, яка буде генерувати 5 випадкових чисел в діапазоні від 0
   до 10(1 рядок через пробіл) і записувати в кінець файла. Викликати функцію
   100 раз, через цикл(файл не повинен перезатиратись, а тільки доповнюватись).
   Результат повинен записуватись в файл test3_result.txt.
'''

from random import randint


def generate_random_string():
    string = ''.join(str(randint(0, 10))+' ' for i in range(5))
    return string[:-1]


if __name__ == "__main__":
    with open('test3_result.txt', 'ab') as file_output:
        for i in range(100):
            file_output.write(bytes(generate_random_string()+'\n', 'utf8'))
    file_output.close()
