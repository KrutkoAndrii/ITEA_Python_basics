'''Написати програму, яка буде зберігати функцію, що рахує суми квадратів
 всіх елементів списку, який йому передається в файл test2.py.'''
import pickle

def count_degree(arrays_of_digits):
    list_of_degrees = [i**2 for i in arrays_of_digits]
    return sum(list_of_degrees)



if __name__ == "__main__":
    '''with open('test2.txt', 'wb') as file_output:
        pickle.dump('def count_degree(arrays_of_digits): \
                        list_of_degrees = [i**2 for i in arrays_of_digits] \
                        return sum(list_of_degrees)', file_output)'''
    with open('test2.txt', 'wb') as file_output:
        pickle.dump('sum([i**2 for i in arrays_of_digits])', file_output)

        #file_output.write(bytes('def count_degree(arrays_of_digits): \
         #               list_of_degrees = [i**2 for i in arrays_of_digits] \
         #               return sum(list_of_degrees)', 'utf8'))
    print(count_degree([2, 3, 5]))
