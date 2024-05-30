from backend.logic.auth import *

def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Change Password")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            scd_password = input("Repeat password: ")

            if manage_user(username, password, scd_password, True):
                print("Registration successful.")
            else:
                print("Registration failed.")
        
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            
            if login_user(username, password):
                print("Login successful.")
            else:
                print("Invalid username or password.")

        elif choice == '3':
            username = input("Enter username: ")
            password = input("Enter password: ")
            scd_password = input("Repeat password: ")
            
            if update_password(username, password, scd_password):
                print("Password changed.")
            else:
                print("Couldnt change password.")
        
        elif choice == '4':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()