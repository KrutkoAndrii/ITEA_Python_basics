# def for matrix
import random


def generate_matrix(length_input, height_input):
    matrix = [[random.randint(0, 100) for i in range(length_input)] for
              z in range(height_input)]
    print(matrix)
    return matrix


if __name__ == "__main__":
    print(" This module not for running!")
