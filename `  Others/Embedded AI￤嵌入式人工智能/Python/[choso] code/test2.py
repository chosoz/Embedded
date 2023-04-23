a=1

def test():
    print('test')

test()
print(test)
print(test())

print(a)
print('%#016X'%id(test))
print('%#016X'%id(a))

# print('%s %d %c %x'%('ivan',10,65,15))  #//老版本格式化输出： 字符串 整型 字符 16进制