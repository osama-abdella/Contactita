#-----------------------------------------------
#------IN THE NAME OF ALLAH---------------------
#-----------------------------------------------
#Contactita

# import modules *
# Asking for username and password from database *
# if ok then login elif return the loop 5 times else break the loop and get out *
# make new file in the path he defines *
# make passwd for file *
# open file with passwd *
# import the name you wanna save *
# import the email you wanna save *
# import the number you wanna save *
# import notes you wanna save *
# save them in a file in the path he defines and then print them in nice block of code on consle *
# if he wanna modify in the file then fine make it ok *
# notify him that the file was in the current path *
# terminate the app *


'''
Simply this tool is saving emails, numbers, important notes, etc.......
'''
import pyfiglet
import termcolor
import sqlite3
import time
import sys
import os.path
import re

print(termcolor.colored(pyfiglet.figlet_format("Contactita"), color="yellow"))
print("By: Osama Abdella\n")
#Login from the database and every user is saved

#Login function
def Log_In():
    tries = 4
    while True:
        tries -= 1
        username = input("Enter your username:# ")
        password = input("Enter your password:# ")
        time.sleep(2)
        if tries == 0:
            print("There is no avaliable tries, come back soon")
            break
        else:
            print("")
        with sqlite3.connect("Quiz.db") as db:
            curser = db.cursor()
        find_user = ("SELECT * FROM user WHERE username = ? AND password = ? ")
        curser.execute(find_user,[(username),(password)])
        results = curser.fetchall()

        if results:
            for i in results:
                print("Welcome " +i[2])
            # return ("exit")
            break
        else:
            # print("Username and password not recognized")
            print(f"Username or password is incorrect, You have {'last' if tries == 0 else {tries}} tries left ")
            again = input("Do you wanna try it again(y/n): ")
            if again.lower() == "n":
                print("GoodBye")
                time.sleep(2)
            # return ("exit")
                break

#NewUser Function
def New_User():
    found = 0
    while found == 0:
        newuser = input("Enter username You prefer=>: ")
        with sqlite3.connect("Quiz.db") as db:
            curser = db.cursor()
        NewUser = ('SELECT * FROM user WHERE username = ?' )
        curser.execute(NewUser, [(newuser)])

        if curser.fetchall():
            time.sleep(2)
            print("Username Taken, Please try again")
        else:
            time.sleep(2)
            found = 1
    firstname = input("Enter your fisrt name:# ")
    surname = input("Enter your sur name:# ")
    password = input("Enter your password:# ")
    password1 = input("Retype your password:# ")
    while password != password1:
        print("Passwords didn't match, please try again: ")
        password = input("Enter your password:# ")
        password1 = input("Retype your password:# ")
    insertData = '''INSERT INTO user(username,firstname,surname,password)
    VALUES(?,?,?,?)
    '''
    curser.execute(insertData, [(newuser), (firstname), (surname), (password)])
    db.commit()

#Chossing from numbers
def menu():
    while True:
        print("Welcome to Contactita")
        Menu =('''
1- create new user
2- login to the tool
3- Exit system\n
        ''')
        userChoise = input(Menu)
        if userChoise == "1":
            New_User()
        elif userChoise == "2":
            Log_In()
            break
        elif userChoise == "3":
            print(termcolor.colored(pyfiglet.figlet_format("Contactita"), color="red"))
            time.sleep(2)
            print("GoodBye!!")
            sys.exit()
        else:
            print("Command not recognized, please try again")
menu()

# Creating file and add the info wanted by the user

def Abslute_Path():
    print(termcolor.colored(pyfiglet.figlet_format("Contactita"), color="blue"))
    #While loops dosn't take while in if make it if
    while True:
        menulista =('''
1-) Create new file
2-) Add data to an existing file 
3-) Show Content of saved file To modify 
4-)Exit Contactita     
        ''')
        choise = input(menulista)
        if choise == "1":
            while True:
                print("ok, Then.......")
                print("=" * 50)
                print(r"Example:{C:\example.txt}")
                print("=" * 50)
                new_path = input("Enter the place you want to save the file with absolute path=>: ")
                if new_path == '':
                    print("No value Given, Try again")
                else:
                    if os.path.exists(new_path):
                        print("This File Already Exists, Try Another Name")
                    else:
                        if os.path.isabs(new_path):
                            print("Creating file.......")
                            print("Alright, file created")
                            fileista = open(new_path, "a")

                            def Addding_data():
                                print("Choose from this list with numbers")
                                while True:
                                    menu1 = ('''
1-) Adding Contact Name
2-) Adding PhoneNumber
3-) Adding E-mail 
4-) Adding WorkPlace
5-) Adding Additional Notes 
6-) Show Content of saved file
7-) Exit Tool
''')
                                    User_input = input(menu1)

                                    if User_input == "1":
                                        time.sleep(1)

                                        def Name_Check():
                                            while True:
                                                Name = input("Enter Name you want to add=> ")
                                                if Name == '':
                                                    print("No Value given, try again")
                                                else:
                                                    print("Done........")
                                                    fileista.write("===========Names===========\n")
                                                    fileista.write(f"{Name} \n")
                                                    break

                                        Name_Check()

                                    elif User_input == "2":
                                        time.sleep(1)

                                        def Number_Check():
                                            while True:
                                                number = input("Enter Phone Number you wannna save=>: ")
                                                if number.isdigit():
                                                    fileista.write("===========Numbers===========\n")
                                                    fileista.write(f"{number} \n")
                                                    print("Done......")
                                                    break
                                                else:
                                                    print("Number Does not contain Any thing, but Numbers, Try again")

                                        Number_Check()

                                    elif User_input == "3":
                                        time.sleep(1)
                                        rex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

                                        def Email_Check():
                                            while True:
                                                email = input("Enter Email you wanna save:# ")
                                                if (re.search(rex, email)):
                                                    fileista.write("===========E-mails===========\n")
                                                    fileista.write(f"{email} \n")
                                                    print("Done.......")
                                                    break
                                                else:
                                                    print(
                                                        "Invalid Email, Try again {Email syntax should be=>: example@example.example}")

                                        Email_Check()


                                    elif User_input == "4":
                                        time.sleep(1)

                                        def Work_Place():
                                            while True:
                                                work = input("Enter workplace you wanna save=>: ")
                                                if re.match("^[A-Za-z0-9_-]*$", work):
                                                    fileista.write("===========Adresses===========\n")
                                                    fileista.write(f"{work} \n")
                                                    print("Done......")
                                                    print("Ok, place saved, if you wanna know the location, google it")
                                                    break
                                                else:
                                                    print("Not recognized, please try again")

                                        Work_Place()

                                    elif User_input == "5":
                                        time.sleep(1)

                                        def Notes_Check():
                                            while True:
                                                notes = input("Enter Your Notes=>: ")
                                                if notes == '':
                                                    print("No value Given, Try Again")
                                                else:
                                                    fileista.write("===========Notes===========\n")
                                                    fileista.write(f"{notes} \n")
                                                    print("Done.......")
                                                    break

                                        Notes_Check()

                                    elif User_input == "6":
                                        time.sleep(1)

                                        def Show_Content():
                                            while True:
                                                show = input("Enter file you wanna open on screen=>: ")
                                                if show == '':
                                                    print("No Value Given, Try Again")
                                                else:
                                                    print("Ok Opening..........")
                                                    os.startfile(show)

                                        Show_Content()


                                    elif User_input == "7":
                                        time.sleep(1)

                                        def Exit_Tool():
                                            print("Bye Friend!!!")
                                            sys.exit()

                                        Exit_Tool()
                                    else:
                                        print("Please Enter a valid number from above")
                            Addding_data()
                            break

                        else:
                            print("Invalid path, Please try again")

        elif choise == '2':
            while True:
                print("=" * 50)
                print(r"Example:{C:\example.txt}")
                print("=" * 50)
                existing_path = input("Enter existing file to add data with absolute path=>: ")
                if existing_path == '':
                    print("No value Given, Try again")
                else:
                    # if os.path.exists(existing_path):
                    #     print("This File Already Exists, Try Another Name")
                    # else:
                        if os.path.isabs(existing_path):
                            print("OK....")
                            filesta1 = open(existing_path, "a")
                            def Addding_data1():
                                print("Choose from this list with numbers")
                                while True:
                                    menu1 = ('''
1-) Adding Contact Name
2-) Adding PhoneNumber
3-) Adding E-mail 
4-) Adding WorkPlace
5-) Adding Additional Notes 
6-) Show Content of saved file
7-) Exit Tool
                                    ''')
                                    User_input = input(menu1)

                                    if User_input == "1":
                                        time.sleep(1)

                                        def Name_Check():
                                            while True:
                                                Name = input("Enter Name you want to add=> ")
                                                if Name == '':
                                                    print("No Value given, try again")
                                                else:
                                                    print("Done........")
                                                    filesta1.write("===========Names===========\n")
                                                    filesta1.write(f"{Name} \n")
                                                    break

                                        Name_Check()

                                    elif User_input == "2":
                                        time.sleep(1)

                                        def Number_Check():
                                            while True:
                                                number = input("Enter Phone Number you wannna save=>: ")
                                                if number.isdigit():
                                                    filesta1.write("===========Numbers===========\n")
                                                    filesta1.write(f"{number} \n")
                                                    print("Done......")
                                                    break
                                                else:
                                                    print("Number Does not contain Any thing, but Numbers, Try again")

                                        Number_Check()

                                    elif User_input == "3":
                                        time.sleep(1)
                                        rex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

                                        def Email_Check():
                                            while True:
                                                email = input("Enter Email you wanna save:# ")
                                                if (re.search(rex, email)):
                                                    filesta1.write("===========E-mails===========\n")
                                                    filesta1.write(f"{email} \n")
                                                    print("Done.......")
                                                    break
                                                else:
                                                    print(
                                                        "Invalid Email, Try again {Email syntax should be=>: example@example.example}")

                                        Email_Check()


                                    elif User_input == "4":
                                        time.sleep(1)

                                        def Work_Place():
                                            while True:
                                                work = input("Enter workplace you wanna save=>: ")
                                                if re.match("^[A-Za-z0-9_-]*$", work):
                                                    filesta1.write("===========Adresses===========\n")
                                                    filesta1.write(f"{work} \n")
                                                    print("Done......")
                                                    print("Ok, place saved, if you wanna know the location, google it")
                                                    break
                                                else:
                                                    print("Not recognized, please try again")

                                        Work_Place()

                                    elif User_input == "5":
                                        time.sleep(1)

                                        def Notes_Check():
                                            while True:
                                                notes = input("Enter Your Notes=>: ")
                                                if notes == '':
                                                    print("No value Given, Try Again")
                                                else:
                                                    filesta1.write("===========Notes===========\n")
                                                    filesta1.write(f"{notes} \n")
                                                    print("Done.......")
                                                    break

                                        Notes_Check()

                                    elif User_input == "6":
                                        time.sleep(1)

                                        def Show_Content():
                                            while True:
                                                show = input("Enter file you wanna open on screen=>: ")
                                                if show == '':
                                                    print("No Value Given, Try Again")
                                                else:
                                                    print("Ok Opening..........")
                                                    os.startfile(show)
                                                    break

                                        Show_Content()


                                    elif User_input == "7":
                                        time.sleep(1)

                                        def Exit_Tool():
                                            print("Bye Friend!!!")
                                            sys.exit()

                                        Exit_Tool()
                                    else:
                                        print("Please Enter a valid number from above")
                            Addding_data1()
                            break

                        else:
                            print("Invalid path, Please try again")
                            break

        elif choise == '3':
            time.sleep(1)
            def Show_Content():
                while True:
                    show = input("Enter file you wanna open on screen=>: ")
                    if show == '':
                        print("No Value Given, Try Again")
                    elif os.path.exists(show):
                        print("Ok Opening..........")
                        os.startfile(show)
                        exit()
                    else:
                        print("This file not in the system, Make sure you typed It correctly, then try again")



            Show_Content()
        elif choise == '4':
            print(termcolor.colored(pyfiglet.figlet_format("Contactita"), color="green"))
            time.sleep(2)
            sys.exit()
        else:
            print("Enter number from above, Try again")

Abslute_Path()


