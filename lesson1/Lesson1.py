
if __name__ == "__main__":
# 1
    print("Задание №1")
    print(3 ** 128 * 2 ** 128)
# 2
    print("Задание №21")
    print('Python'*100)
# 3
    print("Задание №3")
    str = 'molokovoz' #  ну или imput()
    print(str.count('o'))
# 4
    print("Задание №4")
    str = '2,5,1,34,7'
    list = str.split(",")
    list2 = []
    i = 0
    m = (len(list))
    while i <= m-1:
        list2.append(int(list[i]))
        i += 1
    list2.sort()
    print(list2)
# или
    list3 = [2, 4, 1, 22, 6]
    list3.sort()
    print(list3)
# 5
    print("Задание №5")
    print('imput a numeric №1')
    str51 = input()
    if str51.isdigit():
        n51 = int(str51[len(str51)-1])
    else:
        print("Error incoming data ")
        n51 = 0
    print('imput a numeric №2')
    str52 = input()
    if str52.isdigit():
        n52 = int(str52[len(str52)-1])
    else:
        print("Error incoming data ")
        n52 = 0
    print(n51 + n52)
# 6
    print("Задание №6")
    print("input T(kelvin)")
    Kelvin = input()
    print(int(Kelvin)-273)
# 7
    print("Задание №7")
    print("Input a string with ','")
    str7 = input()
    list7 = str7.split(",")
    print(list7)
