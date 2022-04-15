one_number = {
    0:"Zero",
    1:"One",
    2:"Two",
    3:"Three",
    4:"Four",
    5:"Five",
    6:"Six",
    7:"Seven",
    8:"Eight",
    9:"Nine"
}
two_number = {
    10:"Ten",
    11:"Eleven",
    12:"Twelght",
    13:"Therteen",
    14:"Fourteen",
    15:"Fifthteen",
    16:"Sixteen",
    17:"Seventeen",
    18:"Eighteen",
    19:"Nineteen",
    20:"Twenty",
    30:"Thirty",
    40:"Fourty",
    50:"Fifthy",
}




def for_two_numbers_func(user_number):
    # Function for two numbers from user
    singular_number = user_number%10
    decimal_number = (user_number // 10) * 10
    for key in two_number.keys():
        if decimal_number == key:
            list_for_two_numbers.append(two_number[key])
    for key in one_number.keys():
        if singular_number == key:
            list_for_two_numbers.append(one_number[key])


list_for_two_numbers = []
try: # Check if not number 
    number_from_user = int(input("Enter number for convert: "))
    converted_number = str(number_from_user)
    if len(converted_number) == 1: # work if only one number
        for key in one_number.keys():
            if number_from_user == key:
                list_for_two_numbers.append(one_number[key])
    elif number_from_user >= 10 and number_from_user <=20:
        for key in two_number.keys():
            if number_from_user == key:
                list_for_two_numbers.append(two_number[key])
    elif len(converted_number) == 2:
        for_two_numbers_func(number_from_user)
    elif len(converted_number) == 3:
        number_with_three = number_from_user // 100
        two_numbers_get = number_from_user % 100
        if two_numbers_get >= 10 and two_numbers_get <=20:
            for key in two_number.keys():
                if two_numbers_get == key:
                    list_for_two_numbers.append(one_number[number_with_three])
                    list_for_two_numbers.append("Hundred")
                    list_for_two_numbers.append(two_number[key])
        else:
            for key in one_number.keys():
                if number_with_three == key:
                    list_for_two_numbers.append(one_number[key])
                    list_for_two_numbers.append("Hundred")
                    for_two_numbers_func(two_numbers_get)
    else:
        print("No number")  
except:
    print("Enter number")
for word in list_for_two_numbers:
    print(word, end=" ")

    