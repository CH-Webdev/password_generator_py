import random
import string

def create_password(x):
    return ''.join([random.choice(string.ascii_lowercase + string.ascii_uppercase + string.punctuation[3:6] + string.digits) for i in range(x)])

choice = 0

while choice < 6 or choice > 12:

    choice = int(input("How strong do you want your password (6-12) "))

if choice < 6:
    print("Please select an option between 6-12")
elif choice > 12:
    print("Please select an option between 6-12")
else:
    print(create_password(choice))