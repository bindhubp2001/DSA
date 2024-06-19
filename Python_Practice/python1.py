#Program to run ADD stream of number input by user.
# addd stops enter user press q on keyboard

sum = 0
while(True):
  userInput = input("Enter Price..: \n")

  if(userInput != 'q'):
    sum = sum + int(userInput)
    print(f"Order Total So far: {sum} ")

  else:
    print("Total : {sum} Thanks for Shopping")
    break;


