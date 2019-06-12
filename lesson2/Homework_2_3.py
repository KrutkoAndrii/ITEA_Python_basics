# Возвести число в степень с помощью цикла
if __name__ == "__main__":
    user_data_main = input("Enter a numeric for exponented digit ")
    while not user_data_main.isdigit():
        user_data_main = input("Wrong data. Try again: ")
    user_data_ex = input("Enter exponent")
    while not user_data_ex.isdigit():
        user_data_ex = input("Wrong data. Try again: ")
    user_data_main = int(user_data_main)
    user_data_ex = int(user_data_ex)
    result = user_data_main
    if user_data_ex == 0:
        result = 1
    elif user_data_ex > 0:
        for i in range(user_data_ex-1):
            result *= user_data_main
    elif user_data_ex < 0:
        for i in range((user_data_ex * -1) - 1):
            result *= user_data_main
        result = 1 / result
    print("Result is: " + str(result))
