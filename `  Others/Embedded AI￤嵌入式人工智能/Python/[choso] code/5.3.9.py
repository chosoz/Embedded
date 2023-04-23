def func(o):
    o['siteUrl'] = "http://www.csser.com/";
    print(o)
    print('o:',id(o))
    o={};
    print(o)
    print('o:',id(o))    
    o['siteUrl'] = "http://www.popcg.com/";  #//改变的是另一个新创建的对象内容
    print(o)
    print('o:',id(o))
CSSer={};
print(CSSer)
print('CSSer:',id(CSSer))
func(CSSer);  #//o= CSSer;

print(CSSer['siteUrl']); 	
print(CSSer)
print('CSSer:',id(CSSer))