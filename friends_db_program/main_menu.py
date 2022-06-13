from switchlang import switch
from commands_for_db import Commands

command = Commands() # Comands with work DB

# Main menu for work with program
def main():
    """Main function for commands"""
    while True:
        action = input("Enter command for work: ").upper()
        with switch(action) as s:
            s.case("AF", command.add_friend)
            s.case("SF", lambda: print("Add friend")) # not finished!!!
            
            s.case("?", show_menu)
            s.case("E", exit)
            s.default(lambda:print("Enter write command"))


def show_menu():
    print("[AF], Add friend")
    print("[SF], Show friends info")
    print("[?], Show menu")
    print("[E], Exit")


if __name__ == "__main__":
    main()