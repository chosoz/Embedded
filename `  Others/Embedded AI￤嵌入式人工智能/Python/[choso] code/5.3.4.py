def car(): print('dirver car');  #//需先定义，后再使用
def bus(): print('dirver bus');

person ={
  'name':'ivan',
  'driver':car      
}

def change(obj):
  obj['name']='yzg';   #//更改对象的属性
  obj['driver']= bus;  #//更改对象的方法

change(person);
print(person['name']);
person['driver']();