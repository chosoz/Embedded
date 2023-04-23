def sum(*args):
  fir = args[0];
  if(len(args) == 2):
    return args[0] + args[1];
  else:
    return lambda sec:fir + sec;
print(sum(2,3));
print(sum(2)(3));