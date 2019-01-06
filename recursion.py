"""
    Дан словарь, такого вида:
    {
        "name": {
            "first": "One",
            "last": "Drone"
        },
        "job": "scout",
        "recent": {},
        "additional": {
            "place": {
                "zone": "1",
                "cell": "2"}
        }

    }
    привести к такому виду:

    {"name/first": "One",           #one parent
     "name/last": "Drone",
     "job": "scout",                #root key
     "recent": "",                  #empty dict
     "additional/place/zone": "1",  #third level
     "additional/place/cell": "2"}
"""

#рекурсивный метод

test = {'a': 1, 'c': {'a': 2, 'b': {'x': 5, 'y' : 10, 'z':{'a':99}}}, 'd': [1, 2, 3]}

def parse_dict(init, lkey=''):
    ret = {}
    for rKey, val in init.items():
        key = lkey+rKey
        print(key)
        if isinstance(val, dict):
            ret.update(parse_dict(val, key+'_'))
        else:
            ret[key] = val
    return ret

print(parse_dict(test,''))
