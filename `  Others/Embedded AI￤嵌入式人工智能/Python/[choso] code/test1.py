def fn(a):
  def fnn(b):
    return a-b;
  return fnn;
print(fn(20)(5));