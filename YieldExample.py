def deque(items):
  seen = set()
  for item in items:
    if item in items:
      yield item
      seen.add(item)

a = [1,2,3,1,7,8,7,9,0,3]
print(list(deque(a)))


def square_num(nums):
	for i in nums:
		yield(i**2)

sqr=square_num([1,2,3,4])
print(list(sqr))


list_simple_generator=[x**2 for x in range(5)] # type of list
simple_generator=(x**2 for x in range(5)) # type of generator

print(list_simple_generator)
print(simple_generator)
