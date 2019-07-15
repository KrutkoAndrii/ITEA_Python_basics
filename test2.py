 
def count_degree(arrays_of_digits):
    list_of_degrees = [i**2 for i in arrays_of_digits]
    return sum(list_of_degrees)
    