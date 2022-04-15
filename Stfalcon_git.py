
"""
my_list = [4,5,6,7,8,9,10,11,12,     13   ,15,17,19,23,26,28,31,33,34,34]

def find_index(work_list, number):
    min_index = 0
    max_index = len(work_list) - 1 
    while min_index <= max_index:
        mid_index = int((min_index + max_index)/2)
        list_number = work_list[mid_index]
        if list_number == number :
            print(mid_index)
            return mid_index
        if list_number > number:
            max_index = mid_index - 1
        else:
            min_index = mid_index + 1
    print("Dont have this number")
"""           



first_variable = 25

second_variable = 34



variable_for_new_feature = 55555

variable_for_master = 33333

def greet():
    return "Hello world"

print(greet())

def square(num_1,num_2):
    return num_1 * num_2