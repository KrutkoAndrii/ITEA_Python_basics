import random


if __name__ == "__main__":
# 1
    def get_avarage(list):
        list_digit = list.split(",")
        su = 0
        for dig in list_digit:
            print(dig)
            su=su+int(dig)
        return su/len(list_digit)


    print(get_avarage(input('Input string of digit separatet by ,')))
# 2
    array_of_input = [12, 601, 43, 67, 101, 34]


    def get_summ_digit(digit):
        st = str(digit)
        sum_d = 0
        for i in st:
            sum_d += int(i)
        return sum_d


    def sort(array):
        fl = False
        sort_sum = []
        while fl is False:
            fl = True
            for element in array:
                index = array.index(element)
                if index + 1 == len(array):
                    break
                if get_summ_digit(element) > get_summ_digit(array[index+1]):
                    array[index], array[index+1] = array[index+1], array[index]
                    fl = False
        for element_of_array in array:
            sort_sum.append(get_summ_digit(element_of_array))
        return array, sort_sum
    print(array_of_input)
    array_of_input, sort_summ = sort(array_of_input)
    print(array_of_input)
    print(sort_summ)
# 3

    def find_random(min_digit, max_digit):
        array_of_range.append(random.randint(int(min_digit), int(max_digit)))


    def check_input_digit(string):
        user_digit = input(string)
        while not user_digit.isdigit():
            user_digit = input("Wrong data. Try again: ")
        return int(user_digit)


    array_of_range = []
    count_of_element = check_input_digit('input range of list: ')
    min_input = check_input_digit('Input min: ')
    max_input = check_input_digit('Input max: ')
    while max_input < min_input:
        pring('Max should be more then Min. Input new Max')
        max_input = check_input_digit('Input max: ')
    for counter in range(int(count_of_element)):
        find_random(min_input, max_input)
    print(array_of_range)
# 4 есть в примере

