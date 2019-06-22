# Найти сумму элементов матрицы
import random


def check_input_digit(string):
    user_digit = input(string)
    while not user_digit.isdigit():
        user_digit = input("Wrong data. Try again: ")
    return int(user_digit)


def generate_matrix(matrix_rows_number, matrix_columns_number):
    matrix = [[random.randint(0, 100) for i in range(matrix_rows_number)] for z in range(matrix_columns_number)]
    print(matrix)
    return matrix


def get_sum_diagonal(in_matrix, in_side):
    sum_diagonal = 0
    for i_diagonal in range(in_side):
        sum_diagonal += in_matrix[i_diagonal][i_diagonal]
    return sum_diagonal


if __name__ == "__main__":
    # Для упрощения возьмем квадратную матрицу
    side = check_input_digit("Input side of matrix: ")
    incoming_matrix = generate_matrix(side, side)
    print("Sum diagonal of matrix is: "+str(get_sum_diagonal(incoming_matrix, side)))
