high = 100
low = 0
guess = int((high + low)/2)

print("Please think of a number between " + str(low) + " and " + str(high) + "!")
guessing = True
while guessing:
  print("Is your secret number " + str(guess) + "?")
  response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

  if response == 'h':
    high = guess
    guess = int((low + guess)/2)
  elif response == 'l':
    low = guess
    guess = int((high + guess)/2)
  elif response == 'c':
    guessing = False
    print("Game over. Your secret number was: " + str(guess))
  else:
    print("Sorry, I did not understand your input.")