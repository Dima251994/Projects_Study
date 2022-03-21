#Program for guessing number 
import random

def main():
    play_again = "yes"
    while play_again == "yes":
        if play_again != "yes":
            break
        number_from_random = random.randint(0,11)
        tries = 3
        while tries > 0:
            user_number = int(input("Enter number: "))
            if number_from_random == user_number:
                print("You win")
                play_again = input("Play again? ")
            elif number_from_random > user_number:
                print("Слишком маленькое число")
                tries -= 1
            elif number_from_random < user_number:
                print("Слишком большое число")
                tries -= 1
        else:
            print("You lose")
            play_again = input("Play again? ")
    


#def play_again(again):
 ##      main()
    
#play_again(input("Play?").lower())
main()


    


