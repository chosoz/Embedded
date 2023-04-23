class Animal:  #//定义对象 Animal
  name = "animal";
  def breath(this):
    print("can breath from water");

def air():
  print("breath from air");
def change(o):
  print("after change");
  o.breath = air;

obj =  Animal(); #//新建对象实例
print(obj.name);
obj.breath();
change(obj);     #//对象做实参（引用类型传递 是地址传递，指向的是同一实体)
print(obj.name);
obj.breath();	