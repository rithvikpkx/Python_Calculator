def SignUp():
    f = open("CalcData.txt", "r+")
    username = input('Please set a username: ')
    password = input("Please set a password: ")
    f.truncate()
    f.write("Username: " + '-' + username + "-")
    f.write("\nPassword: " + '-' + password + '-')
    f.close()
    print('\nWe have stored your information in our database.')
    Login()

def Login():
    usernamelogin = input("what is your username?: ")
    passwordlogin = input("what is your password?: ")
    r = open("CalcData.txt")
    content = r.readlines()
    if content[1].strip("Password: ") == "-" + passwordlogin + "-" and content[0].strip('Username: ') == "-" + usernamelogin + "-\n":
        print('success\n')
        Calculator()
    else:
        print("Access denied!")
        Login()
    r.close()

def Calculator():
    import time
    x = True
    error = "Error I don't understand."
    print("Welcome to my calculator.\n")
    first_number = input("what is your first number?: ")
    second_number = input("\nwhat is your second number?: ")
    operation = input("\nwhat operation do you want? D|M|S|A: ")
    if not first_number.isnumeric():
        print('Error: The first number must be numeric!')
        Calculator()
    if not second_number.isnumeric():
        print('Error: The second number must be numeric!')
        Calculator()
    if operation.lower() == "d":
        x = False
        print("The solution is: " + (str(float(first_number) / float(second_number))))
    if operation.lower() == "m":
        x = False
        print("The solution is: " + (str(float(first_number) * float(second_number))))
    if operation.lower() == "s":
        x = False
        print('The solution is: ' + (str(float(first_number) - float(second_number))))
    if operation.lower() == "a":
        x = False
        print('The solution is: ' + (str(float(first_number) + float(second_number))))
    if operation.isnumeric():
        print('Error: The operation must be a letter.')
        Calculator()
    if x:
        print("Error: The operation must be either D|M|S|A")
        Calculator()

    def repeat_error():
        repeat = input("\nwould you like to go again? Y|N: ")
        if repeat.lower() == "y":
            Calculator()
        if repeat.lower() == "n":
            print('\nOk have a nice day!\n')
            exit()
        else:
            print(error)
            repeat_error()

    repeat_error()

def Starting_Question():

    Login_Signup = input('Would you like to login or sign up? L|S: ')
    if Login_Signup.lower() == "s":
        SignUp()
    if Login_Signup.lower() == "l":
        Login()
    else:
        print("Sorry, I don't understand.")

Starting_Question()