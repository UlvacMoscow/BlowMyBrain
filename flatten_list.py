
a = [1,[3,3,[4,5],3],2]


def flatten(arr):
    d = []
    def loop(c):
        for x in c:
            if isinstance(x, list):
                loop(x)
            else:
                d.append(x)
    loop(arr)
    return sorted(d)

print(flatten([1, 2, 3]))
print(flatten([1, [2, 2, 2], 4]))
print(flatten([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]))
print(flatten([-1, [1, [-2], 1], -1]))
