list=[  {'name':'test','sex':'male','age':32},
        {'name':'wg','sex':'male','age':28},
        {'name':'xm','sex':'male','age':26},
        {'name':'linda','sex':'female','age':32},
        {'name':'ww','sex':'male','age':37}]
for e in list:
    if e['sex']=='female':
        print('female doesn\'t need to report age')
        continue
    print(e)

