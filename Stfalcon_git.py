
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

"""
class Car():
    def __init__(self, brand, year):
        self.brand_of_car = brand
        self.year_of_car = year

    def change_year(self, new_year):
        self.year_of_car = new_year

    def show_info(self):
        print(self.brand_of_car, self.year_of_car)

car_1 = Car("Skoda", 1987)
car_2 = Car("Mazda", 1999)
car_3 = Car("Honda", 2003)

cars = [car_1, car_2, car_3]

cars[0].show_info()
"""



my_list = [3,1,2,0]

my_list.reverse()
print(my_list)