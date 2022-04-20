
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



# with open("some_file.txt" ,mode="r", encoding="utf-8") as file:
#     #file = open("some_file.txt",mode="r")
#     # reading_line_1 = file.readline()
#     # print(reading_line_1)
#     # reading_line_2 = file.readline()
#     # print(reading_line_2)
#     for line in file:
#         print(type(line))
#         #read_one_line = file.readline()
#         #print(read_one_line)
    

#     #file.close()



class SomeValueError(Exception):
    """Error value too large"""
    #print("Value_Too_Large_Error")
    pass

number = 10
try:
  if number > 3:
     raise SomeValueError
except SomeValueError:
     print("Value too big")  


