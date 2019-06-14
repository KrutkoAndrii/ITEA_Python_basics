import random


def get_avarage(list_in):
    digit_list = list_in.split(",")
    su = 0
    for dig in digit_list:
        print(dig)
        su = su + int(dig)
    return su / len(digit_list)


def get_sum_digit(digit):
    st = str(digit)
    sum_d = 0
    for i in st:
        sum_d += int(i)
    return sum_d


def sort_shell(array):
    sorted_sum = []
    half_len = int(len(array)/2)
    while half_len > 0:
        for i in range(len(array)-half_len):
            j = i
            while j >= 0 and array[j] > array[j+half_len]:
                array[j], array[j+half_len] = array[j+half_len], array[j]
                j -= 1
        half_len = int(half_len/2)
    for element_of_array in array:
        sorted_sum.append(get_sum_digit(element_of_array))
    return array, sorted_sum


def find_random(min_digit, max_digit):
    array_of_range.append(random.randint(int(min_digit), int(max_digit)))


def check_input_digit(string):
    user_digit = input(string)
    while not user_digit.isdigit():
        user_digit = input("Wrong data. Try again: ")
    return int(user_digit)


if __name__ == "__main__":
# 1
    print(get_avarage(input('Input string of digit separatet by ,')))
# 2
    array_of_input = [12, 601, 43, 67, 101, 34, 1]
    print(array_of_input)
    array_of_input, sort_summ = sort_shell(array_of_input)
    print(array_of_input)
    print(sort_summ)
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
# 4 есть в примере
