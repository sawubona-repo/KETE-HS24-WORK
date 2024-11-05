# Example Code: LISTS
# KETE-HS24 /dbe

videoGames = ["Mario", "Sonic", "Joust", "Zelda"]

# Add 'Minecraft' to the start of the list.
videoGames.insert(0,"Minecraft")

# Ask the user to input a number between 0 and 4 and store it in a variable.  Output the item at this position in the list.
gamePos = int(input("Enter a number between 0 and 4."))

#Complex concatentaion with variables and strings here, make sure students are using all the necessary + signs
print("The game at position " + str(gamePos) + " is " + videoGames[gamePos])

# Ask the user to input the name of a video game and store it in a variable.  If this video game is in the list then remove it from the list and output a message .  If it isn't in the list then add it to the end.
game = input("Enter the name of a video game")

if game in videoGames:
  print(game + " was already in the list, so has been deleted.")
  videoGames.remove(game)
else:
  print(game + " wasn't already in the list, so has been added to the end.")
  videoGames.append(game)

# Output the whole list
print(videoGames)