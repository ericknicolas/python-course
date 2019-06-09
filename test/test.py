correct_password = "1234"

name = input("Please enter your name: ")
password = input("Please enter your password: ")

while(password != correct_password):
    password = input("Wrong password!. Please try again: ")

print(f"Hi {name}!. You're log in")