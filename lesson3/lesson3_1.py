# Вывести прямоугольник со сторонами a,b
def check_input_digit(string):
    user_digit = input(string)
    while not user_digit.isdigit():
        user_digit = input("Wrong data. Try again: ")
    return int(user_digit)


if __name__ == "__main__":
    high = check_input_digit("Input high: ")
    lengt = check_input_digit("Input lengh: ")
    for start_position in range(high):
        print("*" * lengt)
