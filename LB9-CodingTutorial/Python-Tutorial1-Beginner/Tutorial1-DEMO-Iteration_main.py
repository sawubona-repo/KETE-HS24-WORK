# Example Code: ITERATION
# KETE-HS24 /dbe

number = 7

# print("I'm thinking of a number, can you guess it?")
guess = int(input("I'm thinking of a number, can you guess it? "))

answer_wrong = "Wrong!"

while guess != number:
  print("Wrong!")  
  
  if guess < number:
    print(answer_wrong +" - Too low!")
  elif guess > number:
    print(answer_wrong + " - Too high!")
    
  guess = int(input("Plz guess again: "))
  
print("Congrats, You guessed it!")


# Give the line number where iteration starts.
  # 4

# What does '!=' mean?
  # Not equal to

# How many variables are there in the code?
  # 2

# How can you tell which lines of code are inside the loop?
  # They are indented

# How many times will the loop repeat?
  # Unknown - until the user inputs '7'

# What has to happen to make the program run the last line of code?
  # The condition on line 4 has to be false (guess and number variables have to contain the same data.)