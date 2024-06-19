import random




def guessing_game():
  print("Welcome to Guessing Game .....")
  secrete_number = random.randint(1,15)
  attempt = 0
  while True:
    guess = int(input("Guess the number between 1-15\n"))
    attempt += 1

    if guess == secrete_number:
      print("Congratulation!!!!!!!!!!")
      break
    elif guess < secrete_number:
      print("Too low")
    else:
      print("Too high")

guessing_game()

