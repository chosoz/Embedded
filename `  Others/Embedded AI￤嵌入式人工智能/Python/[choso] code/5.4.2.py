def fun():
  return {
    'name': 'ivan',
    'driver':lambda str:'can dirver '+str,
  };
print('Person '+ fun()['name']);
print(fun()['driver']('car'));