
a = [1,[3,3,[4,5],3],2]
# c = [a.append(a.pop(a.index(x))) for x in a if isinstance(x, list)]
d=[]

def flatten(arr):
    for x in arr:
        if isinstance(x, list):
            flatten(x)
        else:
            d.append(x)
    d.sort()
    return print(d)

flatten(a)
