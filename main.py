import json
import os
import error_check as ec


# Login class for login page
class Login:
    def __init__(self, name="-", password="-"):
        self.name = name
        self.password = password

    def get_name(self):
        return self.name

    def get_password(self):
        return self.password

    def __str__(self):
        return f"\nName: {self.name}\tPassword: {self.password}"


def menu():
    file_path = "login_info.json"
    i = 0
    while True:
        print(" ________________________")
        print("|                        |")
        print("|        Login Menu      |")
        print("|________________________|")
        print("|                        |")
        print("|       1. Login         |")
        print("|       2. Sign Up       |")
        print("|________________________|")
        print("\nPlease enter the option: ")
        opt = ec.get_input(int)
        if opt == 1:
            if not(os.path.isfile(file_path)):
                print(f"{file_path} does not exists")
            else:
                print("\nLogging up page\n")
                print("Enter your name: ")
                input_name = ec.get_input(str)
                print("Enter your password: ")
                input_password = ec.get_input(str)
                with open(file_path, 'r') as file:
                    i = 0
                    for line in file:
                        loaded_dict = json.loads(line)
                        if loaded_dict['Name'] == input_name and loaded_dict['Password'] == input_password:
                            i += 1
                if i > 0:
                    print("\nLogin Successfully!")
                else:
                    print("\nLogin Failed!")
                break
        elif opt == 2:
            temp_object = Login()
            print("\nSigning up page\n")
            print("Enter your name: ")
            temp_object.name = ec.get_input(str)
            print("Enter your password: ")
            temp_object.password = ec.get_input(str)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as file:
                    for line in file:
                        loaded_dict = json.loads(line)
                        if loaded_dict['Name'] == temp_object.name:
                            i += 1
            if i > 0:
                print("The user is already signed up!")
            else:
                temp_dic = {'Name': temp_object.name, 'Password': temp_object.password}
                with open(file_path, 'a') as file:
                    json.dump(temp_dic, file)
                    file.write('\n')
                    print("Signed up Successful!")
            continue


menu()
