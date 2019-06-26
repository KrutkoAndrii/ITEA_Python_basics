# Как передать копию списка или словаря в функцию?

import random


def get_array(new_array):
    new_array = [random.randint(0, 100) for i in range(10)]
    return new_array


if __name__ == "__main__":
    array_of_digit = [random.randint(0, 100) for i in range(10)]
    print("New array:     " + str(array_of_digit))
    print("Changed array: " + str(get_array(array_of_digit[:])))
    print("Old array:     " + str(array_of_digit))
