#password genertor program
# letter = string.ascii_lettter
# number = string.digits
# special symbols = string.punctuation


import random
import string

print("WELCOME TO THE PASSWORD GENERTOR")
print("SELECT YOUR PASSWORD TYPE")
print("1 - Letters only")
print("2 - Letters + numbers")
print("3 - Letters + Numbers +Special Symbols")

choice = int(input("Enter your choice of password(1 , 2 , or 3) : "))
size = int(input("how many char do you want in password : "))

if choice == 1:
    chars = string.ascii_letters
    password = " ".join(random.choice(chars)for _ in range(size))
    print(f"your password is {password}")
    # " " this is an empty string and with .join method
    # we use _ this becz we do not need to value .we just want to run

elif choice == 2:
    chars = string.ascii_letters + string.digits
    password = " ".join(random.choice(chars)for _ in range(size))
    print(f"your password is {password}")

elif choice == 3:
    chars = string.ascii_letters + string.digits +string.punctuation
    password = " ".join(random.choice(chars)for _ in range(size))
    print(f"your password is {password}")


else:
    print("INVAILD INPUT ! PLEASE CHOOSE ONE choice")    


