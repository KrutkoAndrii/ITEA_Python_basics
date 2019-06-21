''' Без использования методов списков, напишите реализацию таких методов списков: insert, remove. '''


def insert(array, item, position):
    if position < 0 or position > len(array):
        return -1
    array_temp = array[position:]
    del (array[position+1:])
    array[position] = item
    array += array_temp
    return array


def remove(array, item):
    position = 0
    for item_current in array:
        if item_current == item:
            array_temp = array[position+1:]
            del (array[position:])
            array += array_temp
            return array
        position += 1
    else:
        return -1


if __name__ == "__main__":
    array_initial = ['a1', 'a2', 'a3', 'a4']
    print(insert(array_initial, 'b1', 1))
    print(remove(array_initial, 'b1'))
