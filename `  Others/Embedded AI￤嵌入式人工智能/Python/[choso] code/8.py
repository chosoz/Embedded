# //---选取
str='time:2016-ivan';
print(str[1]);   #//选取指定位置的字符
print(str[5:9])  #//选取第5个到第9个间的字符
print(str[5:])
print(str[:9])
print(str[-4:])  #//选取倒数第4个字符开始，直到结束的字符


str='ivan2016 yzg2016'; 
print(str.replace('2016', ''))           #//替换  -> 删除第一个数字2016 
print(str*2) 