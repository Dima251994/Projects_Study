# Программа для добавления товаров в список покупок

buying_list = []


def add(): #Function for adding stuff in listS
    stuff = "yes"
    while True:
        if stuff == "no" or stuff == "NO":
            break
        else:
            print("Input 'no' for stop adding")
            #stuff = input("Enter stuff: ")
            buying_list.append(stuff)
            stuff = input("Enter stuff: ")
            

def remove(): # function for removing stuff from list 
    stuff = "yes"
    while True:
        if stuff == "no" or stuff == "No":
            break
        else:
            buying_list.remove(stuff)
            print("Remove item more ? ")
            stuff = input("Enter what remove: ")


def show(): # for show list
    print("Items in list: ", end="")
    for item in buying_list:
        print(item, sep=",")
    print( )
        

def main():
    while True:
        command = input("Enter command for work with list: ")
        if command == "add":
            add()
        elif command == "remove":
            remove()
        elif command == "show":
            show()
        else:
            break

main()
        
        
