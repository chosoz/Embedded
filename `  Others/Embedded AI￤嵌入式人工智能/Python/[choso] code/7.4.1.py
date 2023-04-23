num=[1,2,3]
def callback(x):
  return x-2

def map(callback,list):
  n =[]
  for v in list:
    n.append(callback(v))
  return n

ret = map(callback,num)
print(ret)