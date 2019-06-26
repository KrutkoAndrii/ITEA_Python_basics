# Найти сумму элементов матрицы
import random


def check_input_digit(string):
    user_digit = input(string)
    while not user_digit.isdigit():
        user_digit = input("Wrong data. Try again: ")
    return int(user_digit)


def generate_matrix(length_input, height_input):
    matrix = [[random.randint(0, 100) for i in range(length_input)]
              for z in range(height_input)]
    print(matrix)
    return matrix


def get_sum_matrix(in_matrix):
    matrix_sum = 0
    for row in in_matrix:
        for num in row:
            matrix_sum += num
    return matrix_sum


def get_sum_matrix_alternative(in_matrix):
    return sum(sum(in_matrix, []))


if __name__ == "__main__":
    length = check_input_digit("Input length of matrix: ")
    height = check_input_digit("Input height of matrix: ")
    incoming_matrix = generate_matrix(length, height)
    print("Sum of matrix is: " + str(get_sum_matrix(incoming_matrix)))
    print("Alternative way sum of matrix is: "
          + str(get_sum_matrix_alternative(incoming_matrix)))
