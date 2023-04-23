def autoAdd():
    count = [0];
    def getCount():
        count[0]+=1;
        return  count[0];
    return getCount;        #//返回函数名（暴露内部信息 ）
p = autoAdd();
# print('call count...',autoAdd()()); #//通过子函数引用，能访问局部变量
# print('call count...',autoAdd()()); #//引用在，其内部的变量将一直保持
# print('call count...',autoAdd()())

print('call count...',p()); #//通过子函数引用，能访问局部变量
print('call count...',p()); #//引用在，其内部的变量将一直保持
print('call count...',p())
