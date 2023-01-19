import random

penalties = 0
guesses = 0
black = 0
white = 0

guess = []
count = 0
repeat = False
invalid = False

colors = ["Red", "Yellow", "Blue", "Green", "Orange", "Pink", "Purple", "Cyan", "Silver", "Teal"]

list = random.sample(range(0, 10), 4)
colors_list = []

for x in range(0, 4):
  colors_list.append(str.lower(colors[list[x]]))

name = input("What is your name: ")

print("Welcome to Master Mind " + name + "!")
print("The code make is here. Available colors are: ")
for x in range(0, len(colors)):
  if (x!=(len(colors)-1)):
    print(colors[x], end=", ")
  else:
    print(colors[x])
    
for y in range(0, len(colors)):
  colors[y] = str.lower(colors[y])

print("You have 15 guesses, total of 5 penalties are allowed but avoid penalties. ")

print("The code maker has selected 4 colors.")

print("You can start guessing " + name)

while (guesses!=15 and penalties!=5):
  print("Enter guess number", guesses+1, end=": ")
  inp = str.lower(input())
  guess = inp.split()
  guesses+=1
  repeat = False
  invalid = False
  
  if (len(guess)==4):  
    for y in range(0, 4):
      count = 0
      count = guess.count(guess[y])
      if (count>1):
        print("Sorry", name, end=", repeated colors are not allowed in this game. One penalty is considered.")
        print('')
        penalties+=1
        print("Penalties =", penalties)
        repeat = True
        break
    if (repeat==False):  
      for y in range(0, 4):
        count = 0
        count = colors.count(guess[y])
        if (count==0):
          print("Sorry", name, end=", cannot recognize the colors you entered. One penalty is considered.")
          print('')
          penalties+=1
          print("Penalties =", penalties)
          invalid = True
          break
      if (invalid==False):
        if (guess==colors_list):
          print("You got 4 blacks", name)
          print("You won the game with", guesses, "guesses and", penalties, "penalties, Congratulations. ")
          exit()
          
        else:
          black = 0
          white = 0
          for y in range(0, 4):
            if (guess[y]==colors_list[y]):
              black+=1
            count = colors_list.count(guess[y])
            if(count==1 and guess[y]!=colors_list[y]):
              white+=1

        print("You got", black, "blacks, and", white, "whites for this guess.")
      
  else:
    print("Sorry", name, end=", you need to enter at least 4 colors for each guess. One penalty is considered.")
    print('')
    penalties+=1
    print("Penalties =", penalties)

if (guesses==15):
  print("Sorry", name, "you ran out of guesses and you lost the game with", penalties, "penalties.")
elif (penalties==5):
  print(name, end=", you lost the game by reaching the maximum number of allowed penalties. ")