from random import randint
from random import choice
import sys

easy = 10
medium = 100
hard = 1000



print("Hello")

difficulty = raw_input("Do you want to play on Easy, Medium, or Hard mode?")
difficulty = difficulty.lower()

if difficulty == "":
  difficulty = choice(["easy", "medium", "hard"])
  print("You are playing in " + difficulty + " mode!")

if difficulty == "easy":
  randomnumber = randint(1, easy)
elif difficulty == "medium":
  randomnumber = randint(1, medium)
elif difficulty == "hard":
  randomnumber = randint(1, hard)

else:
  print("I didn't recognise that.")
  sys.exit()

tries = 0

while True:
  tries+=1
  try:
    guess = int(raw_input("Pick a number:"))
  except:
    sys.exit()
  if randomnumber == guess:
    print("You've got it right in " + str(tries) + " tries!")
    break
  elif guess > randomnumber:
    print("Too high!")
  else:
    print("Too low!")
