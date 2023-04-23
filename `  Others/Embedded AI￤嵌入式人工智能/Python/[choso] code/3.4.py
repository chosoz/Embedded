str1 = 12;
# str2 = str1;    #//赋值是 引用的拷贝(引用是指向实体的地址)
print(id(str1)) #//id() 是查看对象的存储地址
# print(id(str2))
print(str1);  
# print('str2 = ' + str2); 	
str1 = 13;
print(id(str1))
# print(id(str2))
print(str1);  
# print('str2 = ' + str2); 	
