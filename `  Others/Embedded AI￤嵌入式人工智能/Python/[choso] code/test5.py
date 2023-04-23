

# x=1
# print(x,id(x))
# x=x+4
# print(x,id(x))
# def inner():
#     x+=1
#     print(x,id(x))

# inner()

# b=[1,34]
# b=[3,14,2]
# print(b)

train = [50,20,'apple'];
print(train,id(train));
train = [50,20,'apple'];

print(train,id(train));
list = train;
train[2] = 'tv';
print(train,id(train));

print(list,id(list));	 
train = [50,20,'tv'];
print(train,id(train));

print(list,id(list));	