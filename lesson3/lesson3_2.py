# Найти сумму элементов матрицы
import random


def check_input_digit(string):
    user_digit = input(string)
    while not user_digit.isdigit():
        user_digit = input("Wrong data. Try again: ")
    return int(user_digit)


def generate_matrix(length_input, high_input):
    matrix = [[random.randint(0, 100) for i in range(length_input)] for z in range(high_input)]
    print(matrix)
    return matrix


def get_sum_matrix(in_matrix, length_input, high_input):
    sum_matrix = 0
    for i_high in range(high_input):
        sum_line = 0
        for i_length in range(length_input):
            sum_line += in_matrix[i_high][i_length]
        sum_matrix += sum_line
    return sum_matrix


def get_sum_matrix_alternative(in_matrix):
    return sum(sum(in_matrix, []))


if __name__ == "__main__":
    length = check_input_digit("Input length of matrix: ")
    high = check_input_digit("Input high of matrix: ")
    incoming_matrix = generate_matrix(length, high)
    print("Sum of matrix is: " + str(get_sum_matrix(incoming_matrix, length, high)))
    print("Alternative way sum of matrix is: " + str(get_sum_matrix_alternative(incoming_matrix)))
