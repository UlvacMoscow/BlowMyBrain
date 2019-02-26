#додоелать поиск друзей

def check_connection(network, firstFriend, secondFriend):
  networks = create_network(network)
  for unique_group in networks:
    if firstFriend and secondFriend in unique_group:
      return True
  return False




def create_network(network):
  for index, friends in enumerate(network[:- 1]):
    friends = friends[index].split('-')
    next_friends = friends[index + 1].split('-')
    if friends[0] in next_friends or friends[1] in next_friends:
      set(friends, next_friends)
  pass

def init_network(relation):
  pass

# print(set(("dr101", "mr99", "mr99", "out00", "dr101", "out00", "scout1", "scout2", "scout3","scout1", "scout1","scout4", "scout4","sscout", "sscout","super")))

check_connection(
  ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
    "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
   "scout2", "scout3") #== True

check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2", "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "dr101", "sscout") #== False
