from backend.logic.auth import *
from backend.logic.services import *
from backend.security.encrypt import *
from comps import *

def main():
    while True:
        user_id, logged_in = auth()
        if(user_id == -1):
            print("Leaving...")
            break

        if(logged_in == True):
            service_display(user_id)


def auth():
    user_id = 0
    logged_in = False

    while True:
        print("1. Login")
        print("2. Register")
        print("3. Change Password")
        print("-------------------------")
        print("0. Exit")
        print("-------------------------")
        choice = input("Choose an option: ")
        print()

        if choice == '1':
            print("Logging in...")
            username = input("Enter username: ")
            password = input("Enter password: ")
            
            user_id = login_user(username, password)

            if user_id != -1:
                logged_in = True
                space()
                print("Login successful.")
                print()
                break
            else:
                space()
                print("Invalid username or password.")
                print()
        
        elif choice == '2':
            print("Registing new user...")
            username = input("Enter username: ")
            password = input("Enter password: ")
            scd_password = input("Repeat password: ")

            if manage_user(username, password, scd_password, True):
                space()
                print("Registration successful.")
                print()
            else:
                space()
                print("Registration failed.")
                print()

        elif choice == '3':
            print("Changing password...")
            username = input("Enter username: ")
            old_password = input("Enter old password: ")
            password = input("Enter password: ")
            scd_password = input("Repeat password: ")
            
            if update_user_password(username, old_password, password, scd_password):
                space()
                print("Password changed.")
                print()
            else:
                space()
                print("Couldnt change password.")
                print()
        
        elif choice == '0':
            user_id = -1
            space()
            break
        
        else:
            space()
            print("Invalid choice. Please try again.")
            print()

    return  user_id, logged_in


def service_display(user_id):
    while True:
                services = get_services(user_id)
                if(len(services)==0):
                    print("You have no available services.")
                else:
                    print("These are all of your available services:")
                
                for index, service in enumerate(services, start=1):
                    print(f"{index}. {service[0]}")

                print("-------------------------")
                print("-1. Create new Service")
                print("-2. Delete Service")
                print("0. Exit")
                print("-------------------------")
                choice = input("Choose an option: ")

                if(choice == '-1'):
                    service = input("Enter service name: ")
                    account_username = input("Enter account username: ")
                    account_password = input("Enter account password: (enter for automatic generation)")
                    if(create_service(user_id, service, account_username, account_password)):
                        space()
                        print("Successfuly created a new Service")
                        print()
                    else:
                        space()
                        print("Couldn't create the Service")
                        print()

                if(choice == '-2'):
                    service = input("Enter the service id that you want to delete: ")
                    print()
                    if(delete_service(user_id, services[int(service)-1][0])):
                        space()
                        print("Successfuly deleted the Service")
                        print()
                    else:
                        space()
                        print("Couldn't delete the Service")
                        print()

                elif(1 <= int(choice) <= len(services)):
                    space()
                    service_details(services[int(choice)-1], user_id)

                elif(choice == '0'):
                    space()
                    break

                else:
                    space()
                    print("Invalid choice. Please try again.")
                    print()


def service_details(service, user_id):
    while True:
        print("Displaying - " + service[0] + " - information.")
        print("Username: " + service[1])
        print("Password: " + decrypt_password(service[2]))
        print("-------------------------")
        print("1. Change password")
        print("0. Return")
        print("-------------------------")
        choice = input("Choose an option: ")

        if(choice == '1'):
            password = input("Enter password: ")
            if(update_service_password(password, user_id, service[0])):
                space()
                print("Successfuly changed the password")
                print()
                break
            else:
                space()
                print("Couldn´t change the password")
                print()

        elif(choice == '0'):
            space()
            break

        else:
            space()
            print("Invalid choice. Please try again.")
            print()


if __name__ == "__main__":
    main()