def display_players(players):
  print("Player Name    Batting Average")
  print("------------------------------")
  for name in players:
    print(name + "   " + str(players[name]))
players = {}
file = open("Module 12&13 Q6 players.txt", "r")
for line in file:
  data = line.split()
  name = data[0]
  average = float(data[1])
  players[name] = average
file.close()
display_players(players)
