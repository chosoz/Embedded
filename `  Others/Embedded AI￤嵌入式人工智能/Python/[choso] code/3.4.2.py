o1={};
o2=o1;  #//变量里存放的是地址，变量赋值时只是传递了地址。实体只有一个 
o2['name']="CSSer";
print(o1['name']);
print(o1);
print(o2);