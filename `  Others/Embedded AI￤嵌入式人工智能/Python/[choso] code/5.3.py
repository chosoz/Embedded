person = {
 'name':'yzg',
 'age':30
}

def changeName(p):   #//局部变量 p = person  (person里存放的是引用地址 如028）
  p['name'] = 'ivan';

changeName(person);
print(person);