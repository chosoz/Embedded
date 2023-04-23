import random

def guess():
    num=int(input('Please input: scissors(0), stone(1), cloth(2)\n'))
    computer=random.randint(0,2)
    print('computer is',computer)
    if num==computer:
        print('tie')
    elif((num==0 and computer==2) or (num==1 and computer==0) or (num==2 and computer==1)):
        print('You win')
    else:
        print('You lose')

guess()
guess()
guess()
