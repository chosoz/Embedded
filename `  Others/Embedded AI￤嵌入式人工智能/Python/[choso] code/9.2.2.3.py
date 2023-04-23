import struct

fp=open('test.bin','wb')
name = b'lily'
age = 18
sex = b'female'
job = b'teacher'

fp.write(struct.pack('4si6s7s', name,age,sex,job))
fp.flush() #//把缓冲区的内容写入硬盘
fp.close()

fd = open('test.bin','rb')
#// 21 = 4 + 4 + 6 + 7
print(struct.unpack('4si6s7s',fd.read()))
print(fd.tell())        
print(fd.seek(0,0))  
print(fd.read().decode('utf-8'))
fd.close()

