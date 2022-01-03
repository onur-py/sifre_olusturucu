import random


def xx():
    harfler=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+',"<",">","^","+","-"]


    #inp=int(input("Şifrenizin uzunlugu kaç karakter olsun?: "))


    pass_list=[]

    password=""
    for i in range(52):
        pass_list.append(random.choice(harfler))


    for i in range(52):
        pass_list.append(random.choice(symbols))

    for i in range(52):
        pass_list.append(random.choice(numbers))

    random.shuffle(pass_list)

    for i in pass_list:
        password+=i
    return print(password[0:15])

xx()

