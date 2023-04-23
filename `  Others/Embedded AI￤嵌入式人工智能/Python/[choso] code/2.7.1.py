import random

def guess():
    num=int(input("please input suspected big (1) or small (0)"))
    print(num,type(num))

    computer=random.randint(0,1)
    print(computer)
    if(num==computer):
        print("you win")
    else:
        print("you fail")
 

guess()
guess()
guess()
