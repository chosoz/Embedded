obj1 = {'name':'ivan', 'age':30};
obj2 = obj1;            #//赋值只是引用的拷贝，它们还是指向同一实体
obj1['name'] = 'yzg';   #//本身可变 
print('obj1 name = ' + obj1['name']);  
print('obj2 name = ' + obj2['name']); 	#//都改变为'yzg'， 证明指向的是同一实体	