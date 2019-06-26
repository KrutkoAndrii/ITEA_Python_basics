# Вывести прямоугольник со сторонами a,b


from my_package.check_input import check_input_digit

if __name__ == "__main__":
    height = check_input_digit("Input height: ")
    length = check_input_digit("Input length: ")
    for start_position in range(height):
        print("*" * length)
