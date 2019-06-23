'''
    Без использования методов словарей(кроме items),
    напишите  функцию remove по ключу и remove по значению
'''


def remove_by_key(dict_in, key):
    dict_temp = {}
    for key_current, item_current in dict_in.items():
        if str(key_current) == str(key):
            continue
        dict_temp[key_current] = item_current
        dict_in = dict(dict_temp)
    return dict_in


def remove_by_item(dict_in, item):
    dict_temp = {}
    for key_current, item_current in dict_in.items():
        if str(item_current) == str(item):
            continue
        dict_temp[key_current] = item_current
        dict_in = dict(dict_temp)
    return dict_in


if __name__ == "__main__":
    dictionary_initial = {1: 'a1', 2: 'a2', 3: 'a3', 4: 'a4'}
    print(remove_by_key(dictionary_initial, 2))
    print(dictionary_initial)  # Why has the dictionary not changed?
    print(remove_by_item(dictionary_initial, 'a1'))
