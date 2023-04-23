# def sum(**kwargs):
#     print(kwargs)

# sum('a'=1)


# def test(*args):    
#     print(args)   
#     for i in args:
#         print(i)

# test(1,2,3)


def test(**kwargs):
    print(kwargs)
    keys = kwargs.keys()
    value = kwargs.values()
    print(keys)
    print(value)

test(a=1,b=2,c=3,d=4)

