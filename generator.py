def simple_generator(val):
    while val > 0:
        val -= 1
        yield 1


gen_it = simple_generator(4)
print(next(gen_it))
print(next(gen_it))
print(next(gen_it))
print(next(gen_it))
print(next(gen_it))
