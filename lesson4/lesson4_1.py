
''' Пользователь задает случайное число n. Сгенерировать список этой длины и заполнить его 0 и 1 случайным образом.
    Найти самую длинную цепочку из подряд идущих 0 или 1. Вывести эту длину. Для какого максимального значения n,
    ваш алгоритм будет работать меньше чем 1 секунда? '''
import random
import datetime


def check_input_digit(string):
    user_digit = input(string)
    while not user_digit.isdigit():
        user_digit = input("Wrong data. Try again: ")
    return int(user_digit)


def generate_random_of_array(length_of_array):
    print("Generated array...")
    random_array = [random.randint(0, 1) for i in range(length_of_array)]
    # print(random_array)
    return random_array


# Time of searching 0.97 sec for array 20 000 000 items  - CPU i3 6100  8 Gb , Windows 10
def find_the_longest_sequence(array_of_sequence):
    print('Searching...')
    time_start = datetime.datetime.now()
    item = 0
    count_of_item = 0
    max_item = 0
    type_of_max_item = 0
    for item_of_sequence in array_of_sequence:
        if item_of_sequence == item:
            count_of_item += 1
        elif max_item < count_of_item:
            count_of_item += 1
            max_item = count_of_item
            type_of_max_item = item
            item = item_of_sequence
            count_of_item = 0
        else:
            item = item_of_sequence
            count_of_item = 0
    time_finish = datetime.datetime.now()
    elapsed_time = time_finish - time_start
    print("Time of searching is: " + str(elapsed_time))
    print("Max length is: " + str(max_item) + ", and its: " + str(type_of_max_item))


# Time of searching 5.35 sec for array 20 000 000 items  - CPU i3 6100  8 Gb , Windows 10
# but if we have prepared string time decrease to 0.06 sec
def find_the_longest_sequence_alternative(array_of_sequence):
    print('Searching alternative way...')
    time_start = datetime.datetime.now()
    string_of_array = ''.join(str(val) for val in array_of_sequence)
    for type_of_item in ['0', '1']:
        result = 0
        string_of_finding = ''
        while result != -1:
            string_of_finding += type_of_item
            result = string_of_array.find(string_of_finding)
        print('Max length of ' + type_of_item + ' is: ' + str(len(string_of_finding)-1))
    time_finish = datetime.datetime.now()
    elapsed_time = time_finish - time_start
    print("Time of searching is: " + str(elapsed_time))


if __name__ == "__main__":
    length = check_input_digit("Input length of list: ")
    print("Wait...")
    array_by_item = generate_random_of_array(length)
    find_the_longest_sequence(array_by_item)
    find_the_longest_sequence_alternative(array_by_item)
