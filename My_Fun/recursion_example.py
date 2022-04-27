def fact_func(number):
    if number == 1:
        return 1
    else:
        result =  number * fact_func(number-1)
        print(number)
        return result

def recur_func(number):
    if number == 3:
        print("End Matroyshka")
    else:
        print("Top side")
        recur_func(number + 1)
        print("Bottom side")
        