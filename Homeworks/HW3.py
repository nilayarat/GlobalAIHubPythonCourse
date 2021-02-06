# un = "erdem"
# psswrd = 12345
# username = input("Please enter your username")
# password = input("Please enter your password")
# if username == un and password == psswrd:
#     print("Login Successful")
#
database = {"erdem": "12345", "merve": "merve123"}
username = input("Please enter your username")
password = input("Please enter your password")
try:
    if database[username] == password:
        print("Login Successful")
    elif database[username] != password:
        print("Login Failed")
except KeyError:
    print("Login Failed")



