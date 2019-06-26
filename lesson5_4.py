# Найти сумму диагональных элементов матрицы
# напишем программу для неквадратной матрицы
# https://ru.wikipedia.org/wiki/%D0%93%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F
# _%D0%B4%D0%B8%D0%B0%D0%B3%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C
# не сочтите за ошибку длину ссылки
# 1000
# 0102      102000
# 00x0  или 0x0000
# 0201      201000
# 2000


from my_package.check_input import check_input_digit
from my_package.work_with_matrix import generate_matrix


def get_sum_diagonal_matrix(in_matrix, length_input, height_input):
    sum_diagonales = 0
    min_side = length_input if length_input < height_input else height_input
    for i_side in range(min_side):
        sum_diagonales += in_matrix[i_side][i_side] +\
                          in_matrix[height_input-i_side - 1][i_side]
    return sum_diagonales


if __name__ == "__main__":
    length = check_input_digit("Input length of matrix: ")
    height = check_input_digit("Input height of matrix: ")
    incoming_matrix = generate_matrix(length, height)
    print("Sum diagonals of matrix is: "
          + str(get_sum_diagonal_matrix(incoming_matrix, length, height)))
