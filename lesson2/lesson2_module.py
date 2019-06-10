import random
import time
import math


if __name__ == "__main__":
# 1
    min_digit = input('imput min')
    max_digit = input('input max')
    counter = 0
    for counter in range(3):
        print(random.randint(int(min_digit), int(max_digit)))
# 2
    print(time.time())
# 3
    x = int(input('input a numeric'))
    print(math.cos(x) * math.sin(x))
