""" Task solution"""

input_string = input('Введите элементы массива через пробел: ')

elements = input_string.split()
FILTER_CONDITION = 3

def print_result(input_list, result_list):
    """ Print result to console"""
    print(input_list,'->',result_list)

def filter_list(input_list):
    """Filter elements"""
    out_list = []
    for item in input_list:
        if len(item) <= FILTER_CONDITION :
            out_list.append(item)

    return out_list

print_result(elements, filter_list(elements))
