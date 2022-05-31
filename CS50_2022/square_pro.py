def main():
    x = int(input("What x? "))
    print("Squred x is", square(x))

def square(number):
    return number * number # але якщо ми тут змінимо на плюс, тоді будуть помилки


if __name__ == "__main__":
    main()