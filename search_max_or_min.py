import heapq


nums = [2, 34, 11, -3, 0, 2, 90]
print(heapq.nlargest(3, nums)) # [90, 34, 11]
print(heapq.nsmallest(3, nums)) # [-3, 0, 2]


friends = [
    {'name': 'anna', 'age' : 45},
    {'name': 'vitaj', 'age' : 43},
    {'name': 'den', 'age' : 13},
    {'name': 'sen', 'age' : 65},
    {'name': 'sennna', 'age' : 45},
    {'name': 'bana', 'age' : 35},
    {'name': 'sanny', 'age' : 15}
]


young = heapq.nsmallest(2, friends, key=lambda d:d['age'])
olding = heapq.nlargest(2, friends, key=lambda d:d['age'])

print(young)
print(olding)

