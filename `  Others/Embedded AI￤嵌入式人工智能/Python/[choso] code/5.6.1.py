fn = lambda x:x+10;  #//创建匿名函数lambda，让变量fn 指向它
	             #//lambda:冒号 左侧表示函数接收的参数x ,右侧表示函数的返回值x+10
	             #//等价于 def fn(x):return x+10
print(fn(1));
print((lambda x:x+10)(3)) #//可定义调用一气完成

c = lambda x,y=2: x+y    #//默认值
print(c(10))	

L = [(lambda x: x**2),(lambda x: x**4)]  #//字典中
print(L[0](2),L[1](2));
print((lambda x,y: x if x> y else y)(3,5))  #//求最值（类三目运算）