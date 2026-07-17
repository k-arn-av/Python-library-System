from library import Book
from manager import Manager
from users import users

def main():
    print("Welcome to your Library Management System")

    system= Manager()

    system.create_account("232xB", "Arnav")
    system.create_account("232xC", "Zelda")

    print("Login Interface\n")
    if system.login("232xB"):

        Lilo=Book("Lilo","XY","223")
        active_user: users=system.currentUser
        active_user.adds_book(Lilo)

        active_user.library_access.active_book = Lilo
        
        active_user.turns_page()
        active_user.turns_page()
        
        print("\n Testing Account Deletion ---")
        system.delete_account()

    print("\n SYSTEM SIMULATOR SHUTDOWN \n")

if __name__ == "__main__":
    main()



    

