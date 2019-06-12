# Найти сумму диагональных элементов матрицы
# напишем программу для неквадратной матрицы
# https://ru.wikipedia.org/wiki/%D0%93%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D0%B4%D0%B8%D0%B0%D0%B3%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C
# не сочтите за ошибку длину ссылки
# 1000
# 0102      102000
# 00x0  или 0x0000
# 0201      201000
# 2000
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


def get_sum_diagonal_matrix(in_matrix, length_input, high_input):
    sum_diagonales = 0
    min_side = length_input if length_input < high_input else high_input
    for i_side in range(min_side):
        sum_diagonales += in_matrix[i_side][i_side] + in_matrix[high_input-i_side-1][i_side]
    return sum_diagonales


if __name__ == "__main__":
    length = check_input_digit("Input length of matrix: ")
    high = check_input_digit("Input high of matrix: ")
    incoming_matrix = generate_matrix(length, high)
    print("Sum diagonals of matrix is: "+str(get_sum_diagonal_matrix(incoming_matrix, length, high)))
