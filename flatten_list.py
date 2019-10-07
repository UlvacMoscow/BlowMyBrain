a = [1,[3,3,[4,5],3],2]
# c = [a.append(a.pop(a.index(x))) for x in a if isinstance(x, list)]
d=[]
e = []
def conv(c):
    print('111111111')
    print(c)
    for x in c:
        print('x1 ',x)
        if isinstance(x, list):
            print('list')
            b = c.pop(c.index(x))
            conv(b)
        else:
            print('no list')

            d.append(x)
            print('x2 ',x)

    return d

e = conv(a)
print(e)
