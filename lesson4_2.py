# Разбить строку на группы по 3 числа и посчитать суммы каждого первого,
# второго и третьего


def convert_array(array):
    for_del = []
    for item in array:
        try:
            convert_item = float(item)
        except Exception:
            for_del.append(item)
        else:
            array[array.index(item)] = convert_item
    for item_dell in for_del:
        array.remove(item_dell)
    return array


def make_array(string):
    array_dirty = string.split('\n')
    return convert_array(array_dirty)


def make_sum(array):
    array_sum = [0.0, 0.0, 0.0]
    for index in range(0, len(array), 3):
        array_sum[0] += array[index]
        array_sum[1] += array[index+1]
        array_sum[2] += array[index+2]
    return array_sum


if __name__ == "__main__":
    data = """
    0.00002640
    23174.4902
    0.61180654
    0.00002599
    8434.0130
    0.21919999
    0.00002000
    52622.1944
    1.05244388
    0.00001599
    13708.5678
    0.21919999
    0.00001500
    100232.3673
    1.50348550
    """
    array_initial = make_array(data)
    print(array_initial)
    print(make_sum(array_initial))
