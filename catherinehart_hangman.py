import random
game = True
s = ''
x = ','
while game:
  words = ['flower','rainbow','felician university','Girls who Code']
  choice = random.choice(words)
  choice = list(choice)
  correct = []
  for letter in choice:
    correct.append("_ ")
  print()
  print(s.join(correct))

#Number of lives given

  lives = 6
  print("\nYou have " + str(lives)+ " lives remaining")

#Indicate to the player the number of letters in the word

  print("\nThis puzzle has " + str(len(choice)) + " letters")

#Start asking player for a letter

  incorrect = []
  while lives > 0:
    guess = input("\nPlease choose a letter:")
    guess = guess.lower()
  
    if guess not in choice:
      lives = lives - 1
      print("\nThis letter is not in the puzzle. You have " + str(lives) + " lives remaining")
      incorrect.append(guess)
      print("\nIncorrect guesses: " , s.join(incorrect))
      print()
      print(s.join(correct))
    
    if guess in choice:
      index = choice.index(guess)
      correct.insert(index, guess)
      correct.pop(index + 1)
      print("\nIncorrect guesses: " , x.join(incorrect))
      print()
      print(s.join(correct))

# end statement

    if lives == 0:
      print("\nGame over! Here's the correct solution: ")
      print(s.join(choice))
    
    if correct == choice:
      print("\nCongratulations! You solve the puzzle!")
      break

  restart = input("\nWould you like to play again?: ")
  restart = restart.lower()

  if restart == "yes":
    continue

  if restart == "no":
    print("Thank you for playing!")
    break
