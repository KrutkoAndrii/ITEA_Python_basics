'''Написати програму, яка буде зберігати функцію, що рахує суми квадратів
 всіх елементів списку, який йому передається в файл test2.py.'''
def count_degree(arrays_of_digits):
    list_of_degrees = [i**2 for i in arrays_of_digits]
    return sum(list_of_degrees)


if __name__ == "__main__":
    function_to_file = ''' 
def count_degree(arrays_of_digits):
    list_of_degrees = [i**2 for i in arrays_of_digits]
    return sum(list_of_degrees)
     '''
    with open('test2.py', 'w') as file_output:
        file_output.write(function_to_file)
    file_output.close()
