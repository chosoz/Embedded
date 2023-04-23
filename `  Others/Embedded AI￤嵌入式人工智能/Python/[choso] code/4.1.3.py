import random
pcNum = random.randint(0, 100)

def guess_num(num):
    print("right num is ",pcNum)
    if pcNum > num:
        print('你的数字小了')
        return 1
    elif pcNum < num:
        print('你的数字大了')
        return 1
    else:
        print('你赢了')
        return 0

ret = 1
while(1):
    num  = int(input('请输入数字(0-100)\n'))
    print(num,type(num))
    
    if(guess_num(num) ==0):
        break
print('game over')	