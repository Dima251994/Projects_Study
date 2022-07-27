my_vari = 88


def main(): 
    name = input("What youre name? ")
    print(hello(name))
    print(__name__)

def hello(to="world"):
    return f"Hello, {to}" # робимо повернення значення для того щоб можна було тестувати 


if __name__ == "__main__":
    main()
    print("Hello from import")
