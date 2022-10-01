import time

username = "Farhan Khursheed"
password = "hack123"

username_input = input("Please enter the username: ")
password_input = input("Please enter the password: ")

if username_input == username and password_input == password:
    print("Access Granted")
    print("Please wait")
    time.sleep(4)
    print("Loading....")
    time.sleep(3)
    print("...")
    time.sleep(2)
    print("....")
    time.sleep(2)
    print("Loading the security files....")
elif username_input != username and password_input == password:
    print("Invalid username")
elif username_input == username and password_input != password:
    print("Invalid password")
else:
    print("Invalid input")