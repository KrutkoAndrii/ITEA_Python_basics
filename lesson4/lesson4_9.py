''' Напишите функцию, которая сортирует массив рекурсивно.'''


def sort_shell(array,half_len=-1):
    if half_len == -1:
        half_len = int(len(array)/2)
    if half_len > 0:
        for i in range(len(array)-half_len):
            j = i
            while j >= 0 and array[j] > array[j+half_len]:
                array[j], array[j+half_len] = array[j+half_len], array[j]
                j -= 1
        half_len = int(half_len/2)
        sort_shell(array, half_len)
    else:
        return array
    return array


if __name__ == "__main__":
    array_unsorted = [32, 9, 1, 33, 4, 0, 2, 6, 0, 5]
    print(sort_shell(array_unsorted))
