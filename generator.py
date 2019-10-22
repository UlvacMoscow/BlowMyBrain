def simple_generator(val):
    while val > 0:
        val -= 1
        yield val


gen_it = simple_generator(4)
print(type(gen_it))
print(next(gen_it))
print(next(gen_it))
print(next(gen_it))
print(next(gen_it))

a = [1, 2, 3, 4, 5]
print(type(a))

b = (i for i in a if i % 2 == 0)
print(type(b))
print(next(b))
print(next(b))
print(next(b))
