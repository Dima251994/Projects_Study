from colorama import Fore

def get_price(message): # функция для праильного принятия цены когда напишут
    # аргумент принимает сообщение которое нужно отобразить 
    styled_message = "{}{}{}".format(Fore.BLUE, message, Fore.RESET)

    while True:
        input_string = input(styled_message) # запркшивает число

        try:
            return float(input_string.strip()) # пробует вернуть float
        except:
            print(Fore.RED, "Enter number please", Fore.RESET)