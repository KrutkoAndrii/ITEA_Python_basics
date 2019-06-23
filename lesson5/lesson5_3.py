# Найти сумму элементов матрицы

from my_package.check_input import check_input_digit
from my_package.work_with_matrix import generate_matrix


def get_sum_diagonal(in_matrix, in_side):
    sum_diagonal = 0
    for i_diagonal in range(in_side):
        sum_diagonal += in_matrix[i_diagonal][i_diagonal]
    return sum_diagonal


if __name__ == "__main__":
    # Для упрощения возьмем квадратную матрицу
    side = check_input_digit("Input side of matrix: ")
    incoming_matrix = generate_matrix(side, side)
    print("Sum diagonal of matrix is: "+str(get_sum_diagonal(incoming_matrix,
                                                             side)))
