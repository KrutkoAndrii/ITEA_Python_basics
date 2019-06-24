# Найти сумму элементов матрицы


from my_package.check_input import check_input_digit
from my_package.work_with_matrix import generate_matrix


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
    print("Alternative way sum of matrix is: " + str(get_sum_matrix_alternative(
        incoming_matrix)))
