import sys
import random
from operator import concat

user = {
    "id":[],
    "username":[],
    "email":[],
    "password":[],
    "used for":[],
    "tag":[]
}

UPPER_CHARACTERS = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
LOWER_CHARACTERS = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
NUMBERS = ["0","1","2","3","4","5","6","7","8","9"]
SYMBOLS2 = ["!","@","#","$","%","^","&","*","(",")",":","<",">","`","\\","\"","`"]
SYMBOLS = "!@#$%^&*()_-=+\"\\'>?<,[]{}`"

def initialization():
    global data
    global user
    try:
        with open("data", "r", encoding="utf-8") as data_file:
            data = data_file.read().splitlines()
            if len(data) == 0:
                print("No data found")
            elif len(data) >= 6:
                for line in range(0, len(data), 6):
                    if line + 5 < len(data):
                        user["id"].append(data[line])
                        user["username"].append(data[line + 1])
                        user["email"].append(data[line + 2])
                        user["password"].append(data[line + 3])
                        user["used for"].append(data[line + 4])
                        user["tag"].append(data[line + 5])
            else:
                print("Storred data is corrupted")
                data_file.close()
                with open("data", "w", encoding="utf-8") as data_file:
                    data_file.close()
    except FileNotFoundError:
        with open("data", "w", encoding="utf-8") as data_file:
            data_file.close()

def add_account():
    global data
    global user
    generate_id = True
    while generate_id:
        temp_id = random.randint(100000000, 999999999)
        temp_id = str(temp_id)
        if temp_id not in user["id"]:
            generate_id = False
    while True:
        temp_username = input("Enter your username: ").strip()
        if temp_username == "":
            print("Invalid username: Username can't be empty")
            continue
        elif len(temp_username) > 30:
            print("Invalid username: Username can't be this long")
            continue
        elif len(temp_username) < 3:
            print("Invalid username: Username can't be this short")
            continue
        else:
            break
    while True:
        temp_email = input("Enter your email: ").strip()
        if temp_email == "":
            print("Invalid email adress")
        elif temp_email.find("@") == -1:
            print("Invalid email adress")
            continue
        elif temp_email.find(".") == -1:
            print("Invalid email adress")
            continue
        elif len(temp_email) > 30:
            print("Invalid email adress")
            continue
        elif len(temp_email) < 8:
            print("Invalid email adress")
        else:
            break
    while True:
        temp_password = input("Enter your password: ").strip()
        if len(temp_password) < 6:
            print("Invalid password length")
        elif len(temp_password) > 30:
            print("Invalid password length")
        elif temp_password == "":
            print("Invalid password")
        else:
            break
    while True:
        temp_used_for = input("For what is this account used for (ex. game name) :").strip().capitalize()
        if len(temp_used_for) < 3:
            print("Invalid description")
            continue
        elif len(temp_used_for) > 30:
            print("Invalid description")
            continue
        else:
            break
    while True:
        if temp_username in user["username"] and temp_email in user["email"]:
            print("Error: This account already exists in list")
            return(0)
        else:
            break
    while True:
        print("""
        1. Game
        2. Email
        3. App
        4. Phone
        5. Website
        6. Other
        """)
        try:
            temp_tag = int(input("Please select"))
            if temp_tag == 1:
                temp_tag = "Game"
                break
            elif temp_tag == 2:
                temp_tag = "Email"
                break
            elif temp_tag == 3:
                temp_tag = "App"
                break
            elif temp_tag == 4:
                temp_tag = "Phone"
                break
            elif temp_tag == 5:
                temp_tag = "Website"
                break
            elif temp_tag == 6:
                temp_tag = "Other"
                break
            else:
                print("Invalid Option")
                continue
        except ValueError:
            print("Insert a number")
            continue
    with open("data", "a", encoding="utf-8") as f:
        f.write(temp_id + "\n")
        f.write(temp_username + "\n")
        f.write(temp_email + "\n")
        f.write(temp_password + "\n")
        f.write(temp_used_for + "\n")
        f.write(temp_tag + "\n")
        f.close()
        user.clear()
        user = {
            "id": [],
            "username": [],
            "email": [],
            "password": [],
            "used for": [],
            "tag": []
        }
        initialization()
        return(0)

def search_account():
    while True:
        print("""
        1. Search by Account ID
        2. Search by Username
        3. Cancel
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            search = input("Insert your account ID: ")
            if search in user["id"]:
                temp_search = user["id"].index(search)
                print(f"{user["id"][temp_search]} - {user['username'][temp_search]} - {user['email'][temp_search]} - {user['password'][temp_search]} - {user['used for'][temp_search]} - {user['tag'][temp_search]}")
                input("Press any key to continue")
                return(0)
            elif search not in user["id"]:
                print("Invalid ID")
                return(0)
        elif choice == "2":
            search = input("Insert your username: ")
            if search in user["username"]:
                temp_search = user["username"].index(search)
                print(
                    f"{user["id"][temp_search]} - {user['username'][temp_search]} - {user['email'][temp_search]} - {user['password'][temp_search]} - {user['used for'][temp_search]} - {user['tag'][temp_search]}")
                input("Press ENTER to continue")
                return(0)
            elif search not in user["username"]:
                print("Username not found")
                return(0)
        elif choice == "3":
            return(0)


def delete_account():
    global user
    delete_account = input("Insert the Account ID: ")
    if delete_account in user["id"]:
        x = user["id"].index(delete_account)
        user["id"].pop(x)
        user["username"].pop(x)
        user["email"].pop(x)
        user["password"].pop(x)
        user["used for"].pop(x)
        user["tag"].pop(x)
        with open("data", "w", encoding="utf-8") as f:
            for i in range(len(user["id"])):
                f.write(user["id"][i] + "\n")
                f.write(user["username"][i] + "\n")
                f.write(user["email"][i] + "\n")
                f.write(user["password"][i] + "\n")
                f.write(user["used for"][i] + "\n")
                f.write(user["tag"][i] + "\n")
            f.close()
            return(0)

def generate_lower(password_lenght_divided):
    lower_pwd = ""
    for i in range(password_lenght_divided):
        lower_pwd = lower_pwd + random.choice(LOWER_CHARACTERS)
    return(lower_pwd)

def generate_password():
    while True:
        try:
            temp_answer = int(input("How long should the password be (max 32 characters) : "))
            if temp_answer == "":
                print("Invalid input")
                continue
            elif temp_answer > 32:
                print("Password can't be longer than 32 characters")
            elif temp_answer <= 0:
                print("Password can't be empty")
                continue
            elif temp_answer < 6:
                print("Password can't be less than 6 characters")
            else:
                print("Should the password contain special characters?")
                has_special = input("Y/n").upper()
                if has_special == "Y":
                    has_special = True
                else:
                    has_special = False
                print("Should the password contain numbers ?")
                contains_numbers = input("Y/n").upper()
                if contains_numbers == "Y":
                    contains_numbers = True
                else:
                    contains_numbers = False
                print("Should the password contain upper characters?")
                contains_upper = input("Y/n").upper()
                if contains_upper == "Y":
                    contains_upper = True
                else:
                    contains_upper = False
                password_lenght_divided = temp_answer // 4
                password_lenght_remaining = temp_answer % 4

                lower_pwd = generate_lower(password_lenght_divided)
                if has_special:
                    symbol_pwd = ""
                    for i in range(password_lenght_divided):
                        symbol_pwd = symbol_pwd + random.choice(SYMBOLS2)
                if has_special == False:
                    symbol_pwd = generate_lower(password_lenght_divided)
                if contains_numbers:
                    number_pwd = ""
                    for i in range(password_lenght_divided):
                        number_pwd = number_pwd + random.choice(NUMBERS)
                if contains_numbers == False:
                    number_pwd = generate_lower(password_lenght_divided)
                if contains_upper:
                    upper_pwd = ""
                    for i in range(password_lenght_divided):
                        upper_pwd = upper_pwd + random.choice(UPPER_CHARACTERS)
                if contains_upper == False:
                    upper_pwd = generate_lower(password_lenght_divided)
                password = lower_pwd + symbol_pwd + number_pwd + upper_pwd
                password = list(password)
                random.shuffle(password)
                password = "".join(password)
                for i in range(password_lenght_remaining):
                    password = password + random.choice(password)
                return(password)
        except ValueError:
            print("Insert a number")
            continue


def main_menu():
    while True:
        print("""
        1. Add account
        2. Show accounts
        3. Search account
        4. Delete account
        5. Generate password
        6. Quit
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            choice = add_account()
        elif choice == "2":
            for i in range(len(user["id"])):
                print(f"{i}.{user['username'][i]} - {user['email'][i]} - {user['password'][i]} - {user['used for'][i]} - {user['tag'][i]} - ID: {user['id'][i]}")
            input("Press ENTER to continue")

        elif choice == "3":
            choice = search_account()
        elif choice == "4":
            delete_account()
        elif choice == "5":
            password = generate_password()
            print(password)
            input("Press ENTER to continue")
        elif choice == "6":
            sys.exit("See you soon !")
        elif choice == "0":
            continue
        else:
            print("Invalid choice")
            continue

if __name__ == "__main__":
    initialization()
    main_menu()
