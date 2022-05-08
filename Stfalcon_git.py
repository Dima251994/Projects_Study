
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



class Office():
    workers = []
    def __init__(self):
        pass

    def add_worker(self, employee):
        self.workers.append(employee)

    def get_worker(self, index):
        if index < len(self.workers):
            self.workers[index].show_info()
        else:
            print("Not found")



class Employee():
    count_of_employee = 0
    def __init__(self, name, salary):
        self.name_of_employee = name
        self.salary_of_employee = salary
        Employee.count_of_employee += 1
        
    
    def show_count(self):
        print("Total employee:", Employee.count_of_employee)
    
    def show_info(self):
        print(f"Name: {self.name_of_employee}, Salary: {self.salary_of_employee}")



office = Office()
office.add_worker(Employee("Derek", 1300))
office.add_worker(Employee("John", 1600))
office.add_worker(Employee("Bob", 2300))


office.get_worker(6)



