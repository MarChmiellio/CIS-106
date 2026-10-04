def compute_batting_average(hits, at_bats):
  batting_average = hits / at_bats
  return batting_average
player_count = 0
answer = input("Do you want to enter a player? Enter yes or no: ")
while answer == "yes":
  last_name = input("Enter player's last name: ")
  hits = int(input("Enter number of hits: "))
  at_bats = int(input("Enter number of at bats: "))
  batting_average = compute_batting average(hits, at_bats)
  print("Player:", last_name)
  print("Batting Average:", round(batting_average, 3))
  player_count = player_count + 1
  answer = input("Do you want to enter another player? Enter yes or no: ")
print("Number of Players Entered:", player_count)
