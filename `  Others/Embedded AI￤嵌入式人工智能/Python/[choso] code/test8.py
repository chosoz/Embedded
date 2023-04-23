# from sum import  add,sum    #//从模块sum.py中导入 add 和sum函数



# //sum.py 库
# def add(a,b):
#     print(a+b)
#     return a+b

# def sum(n):
#     sum = 0
#     for i in range(n + 1):
#         sum += i
#     print(sum)

# if __name__ == '__main__':  # //做主程序入口(调用者是自己时才执行)
#     sum(add(2,3))


# if __name__ == '__main__':  # //做测试代码(调用者是自己时才执行)
#     sum(3)
#     add(1,2)



# for i in range(5):
#     print(i)


import os

for(dirname, subdir, subfile) in os.walk('D:\Users\Choso\OneDrive\My Code\Python\[choso] code'):  #//  wark返回（当前目录名称,子目录名称,子文件名称）
    print('dirname is %s, subdir is %s, subfile is %s' % (dirname, subdir, subfile))
    for f in subfile:
        print(os.path.join(dirname, f))  #//将多个路径组合后返回	










