all_solutions = []

def get_tuple_tuples(*args):

    l = []
    for elem in args:
        l.append(tuple(elem.split('-')))
        return tuple(l)


t1 = get_tuple_tuples("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2","scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super")

print(t1)
def recursion():
    solution = False
    temp = []
    for el in t1:
        solution = False
        if temp == []:
            temp.append(el[0])
            temp.append(el[1])
            continue

            for uniq_marker in el:
                if uniq_marker in temp:
                    solution = True
                    print('Solution = true, uniq_marker', uniq_marker)
                    continue
                    if not uniq_marker in temp and solution:
                        print('append list uniq_marker', uniq_marker)
                        temp.append(uniq_marker)
                        continue
                    else:
                        print("other sociacl network")


print("my shit code ", temp)


# prev = None, None
# l2 = []
# for el in t1:
#   if prev[0] in el or prev[1] in el:
#     s = set()
#     s |= set([prev[0], prev[1]])
#     print(s)
#   prev = el
#   # l2.append(s)
#  # prev = el

# print(s)
# print(l2)


# check_connection(

#     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",

#      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),

#     "scout2", "scout3") == True

# check_connection(

#     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",

#      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),

#     "dr101", "sscout") == False
