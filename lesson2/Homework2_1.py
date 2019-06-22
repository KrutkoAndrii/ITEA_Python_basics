# Выводить буквы строки, до первой заглавной

if __name__ == "__main__":

    string_input = input('Eenter a line with capital letters: ')
    for char_from_string in string_input:
        if char_from_string.islower():
            print(char_from_string, end='')
            continue
        break
