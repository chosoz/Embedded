//my_module.py   定义自己的模块
def fn():
  print('fn go')

person ={'name':'ivan','age':30}		

class Animal:     
  name = 'animal'  
  def eat(this):   
    print(this.name," can eat")
  def breath(this):
    print(this.name," can breath") 

//use.py   使用模块
import  my_module  #//导入模块
my_module.fn()     #//访问模块里对象

import my_module as m  #//用m做模块假名（使用简洁) 
obj = m.Animal()
obj.eat()

from my_module import person #//只导入模块里指定对象
print(person)
