def sum(*args):
    ret=0
    for obj in args:
        print(obj)
        ret+=obj

    print(ret)
    return ret

sum(1)
sum(1,2,4)