class Person:
    name='lili'
    age=30
    def sing(self):
        print(self.name,'can sing')

p1=Person() #
p2=Person()

print(p1.name,p1.age)
p1.sing()
p1.addr="chengdu"
print(p1.addr)
