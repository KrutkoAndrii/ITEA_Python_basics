import math


if __name__ == "__main__":

# 1
    for i in range(11):
        print(i**2)
# 2
    i = 0
    while True:
        i += 1
        if i**2 > 1000:
            break
        else:
            print(i**2)
# 3
    st = input('imput a numeric ')
    n = math.sqrt(int(st))
    while n > 10:
        print(n)
        n = math.sqrt(n)
# 4
    print('Task 4')
    st = input('input a string ')
    for i in st:
        if i.isupper():
            print(i, end='')
# 5
    print('Task 5')
    st = input('input line of numeric separated by ,')
    st_digit = st.split(',')
    sum_all = 0
    for st_dig in st_digit:
        if st_dig.isdigit():
            sum_all += int(st_dig)
    print(sum_all)
# 6
    print('Task 6')
    fl = 0
    i = 0
    while i < 20:
        if fl == 4:
            print(i, end=' ')
            fl=0
        i += 1
        fl += 1
# 7
    print('Task 7')
    dg_count = 0
    dg_sum = 0
    st = '1'
    while int(st) != 0:
        st = input('input a numeric ')
        if st.isdigit():
            dg_count+=1
            dg_sum += int(st)
        else:
            st = '0'
    if dg_count != 0:
        print('count:'+str(dg_count)+' sum: '+str(dg_sum)+' avr '+str(dg_sum/dg_count))
# 9
    print('Task 9')
    count = input("Input a numeric ")
    fibon_f = 0
    fibon_s = 1
    print('1')
    for i in range(int(count) - 1):
        fibon=fibon_f+fibon_s
        print(fibon, end=' ')
        fibon_f = fibon_s
        fibon_s = fibon
