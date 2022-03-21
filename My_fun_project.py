# Программа для добавления товаров в список покупок

buying_list = []

def add():
    condition = "yes"
    while condition == "yes":
        stuff = input("Enter what add: ")
        buying_list.append(stuff)
        condition = input("Enter more stuff? ").lower()
        for item in buying_list:
            print(f"Was added {item}")

def remove():
    condition = "yes"
    while condition == "yes":
        stuff = input("Enter what add: ")
        buying_list.remove(stuff)
        condition = input("Enter more stuff? ").lower()

    

add()
    
        
