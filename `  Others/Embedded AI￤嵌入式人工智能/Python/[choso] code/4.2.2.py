a, b = 0, 1   #//多重赋值， 拆解为  a=0;  b=1; 
while a < 10:
    print(a)
    # a, b = b, a+b		
    a=b;   b=a+b