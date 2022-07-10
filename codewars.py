# def paperwork(paperworks, pages):
#     if paperworks <0 or pages <0:
#         return 0
#     return paperworks * pages

# print(paperwork(5,5))


# def string_to_array(s):
#     return s.split(" ")

# print(string_to_array("d"))


# def find_smallest_int(arr):
#     return min(arr)

# print(find_smallest_int([34, -345, -1, 100]))



# def remove_smallest(numbers):
#     if numbers == []:
#         return numbers
#     else:
#         new_list = numbers[:]
#         smallest_number = min(new_list)
#         new_list.remove(smallest_number)
#         return new_list

# my_list = [1, 2, 3, 4, 5]

# print(id(my_list))
# print(id(remove_smallest(my_list)))

#Doubled numbers and dont touch original list!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def maps(numbers):
#     index = 0
#     for number in numbers:
#         doubled = number + number
#         numbers[index] = doubled
#         index += 1
#     return numbers
        

# give_list = [1, 2, 3]
# print(id(give_list))


# print(id(maps(give_list)))


#Якщо висота і ширина однакові тоді повернути площу а якщо різні, тоді периметр!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# def area_or_perimeter(lenght , width):
#     if lenght == width:
#         return lenght * width
#     else:
#         return (lenght + width) * 2

# print(area_or_perimeter(6,10))


#Прибрати всі стрічки зі списку, залишити тільки цифри!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# def filter_list(my_list):
#     copy_list = my_list[:]
#     for item in copy_list:
#         if type(item) == str:
#             my_list.remove(item)
#     print(my_list)

# filter_list([1,2,'aasf','1','123',123])


#Сума двох найменших чисел зі списку!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# def sum_two_smallest_numbers(numbers):
#     first_min_number = min(numbers)
#     numbers.remove(first_min_number)
#     second_min_number = min(numbers)
#     return first_min_number + second_min_number


# def sum_two_smallest_numbers_second_version(numbers):
#     print(sorted(numbers))
#     return sum(sorted(numbers)[:2])

# sum_two_smallest_numbers_second_version([19, 5, 42, 2, 77])
# sum_two_smallest_numbers([19, 5, 42, 2, 77])


#Звір повинен принести блюдо яке розпочинається з його імені!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# def feast(beast, dish):
#     if beast[0] == dish[0] and beast[-1] == dish[-1]:
#         return True
#     else:
#         return False

# print(feast("tbph", "yeuimogdlh"))




#Повертає суму чисел зі списку!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# def sum_array(a):
#     return sum(a)

# print(sum_array([]))



#Створити функцію яка перевіряє чи є слово ізограмою, слово яке не повторює букви в словах!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# def is_isogram(string : str):
#     string = string.lower()
#     for item in string:
#         if string.count(item) > 1:
#             return False
#     return True

# #Best Practice
# def is_isogram(string):
#     return len(string) == len(set(string.lower()))


#Повернути спиок де два числа це сума позитивних чисел і негативних!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# def count_positives_sum_negatives(arr):
#     result_list = []
#     if arr == []:
#         return result_list
#     positive_counter = 0
#     negative_summary = 0
#     for number in arr:
#         if number > 0:
#             positive_counter +=1
#         else:
#             negative_summary +=number
#     result_list.append(positive_counter)
#     result_list.append(negative_summary)
#     return result_list
       # Трохи оптимізовна версія #
# def count_positives_sum_negatives(arr):
#     if arr == []:
#         return []
#     positive_counter = 0
#     negative_summary = 0
#     for number in arr:
#         if number > 0:
#             positive_counter +=1
#         else:
#             negative_summary +=number
#     return [positive_counter, negative_summary] # замість того щоб ініціалізувати список як вище і додавати ми можемо одразу повернути список


# print(count_positives_sum_negatives([1,2,3,4,5,6,-13,-14,-14,-15,-43]))

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

