from collections import defaultdict, OrderedDict
import json


d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}

e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}


c = defaultdict(list)

c['a'].append(1)
c['a'].append(2)
c['b'].append(4)

j = defaultdict(set)

j['a'].add(1)
j['a'].add(2)
j['b'].add(4)

print(c, j)


orderDict = OrderedDict()

orderDict['first'] = 1
orderDict['second'] = 2
orderDict['third'] = 3
orderDict['fourth'] = 4
orderDict['fivth'] = 5

print(orderDict)

jsdict = json(orderDict)

print(jsdict)
