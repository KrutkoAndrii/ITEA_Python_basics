'''
 Без использования методов строк, напишите реализацию таких методов строк:
 replace, split, find. Напишите функцию remove по индексу и по подстроке.
  '''


def replace(string, substring, substring_new, count_of_replace=-1):
    string_new = ''
    counter = 0
    string_len = len(substring)
    string_index = 0
    while string_index < len(string):
        if string[string_index:string_index + string_len] == substring:
            string_new += substring_new
            string_index += string_len
            counter += 1
            if counter == count_of_replace:
                return string_new + string[string_index:]
        else:
            string_new += string[string_index]
            string_index += 1
    return string_new


def split(string, separator, count_of_split=-1):
    list_result = []
    string_new = ''
    string_len = len(str(separator))
    string_index = 0
    counter = 0
    while string_index < len(string):
        if string[string_index:string_index + string_len] == separator:
            list_result.append(string_new)
            string_new = ''
            string_index += string_len
            counter += 1
            if counter == count_of_split:
                list_result.append(string[string_index:])
                return list_result
        else:
            string_new += string[string_index]
            string_index += 1
    list_result.append(string_new)
    return list_result


def find(string, substring, start=0, end=-1):
    if end == -1:
        end = len(string)
    string_index = 0
    string_len = len(str(substring))
    while string_index < len(string[start:end]):
        if string[string_index +
                  start:string_index + start + string_len] == substring:
            return string_index+start
        string_index += 1
    return -1


if __name__ == "__main__":
    print(replace('This is the island of istanbul', 'is', 'was', 2))
    print(split('This is the island of istanbul', ' ', 2))
    print(find('This is the island of istanbul', 'the', 7, 17))
