from collections import deque


q = deque([1,2,3,4,5,6], maxlen=3)


print(q)
q.append(7)
print(q)
q.appendleft(7)
print(q)

def search(lines, pattern, history=3):
    prev_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, prev_lines
        prev_lines.append(line)


a = 'я шел домой пъяныйб и шел шел!'
b = 'шел'

print(search(a,b)) #return generator objects