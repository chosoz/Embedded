# train = [50,20,'apple']
# train[0]={'name':'wangwei',587:(32,42,[3,2])}
# print(train)

train = [50,20,'apple'];
train[1] ={'name':'lili','age':30}
print(train)


#//可把函数名，看成指向代码块的引用
def gogo():
    print("i can gogogo")
    
train[1]['teach']=gogo  
print(train)
train[1]['teach']()		


