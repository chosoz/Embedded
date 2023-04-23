# a=true
# b=not a
# print(b)

# a='iphone'

# print(a[0:3])


x = 'iphone';  #//或x = 30 , x = true;
def fn(v):     #//函数参数: ()  --  输入（做事需要什么东西， 如 v） 
  print(v,' type: ',type(v));
  v = 'android';
  print(v)
fn(x);  #//传字符串(或 数值6000 布尔值） 
print(x);		