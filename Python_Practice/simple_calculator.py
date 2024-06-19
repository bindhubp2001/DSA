def calculator(number1,number2):
  if choice == 1:
    sum = number1 + number2
    print(f"SUM is {sum}")

  elif choice == 2:
    sub = number1 - number2
    print(f"SUB is {sub}")

  elif choice == 3:
    mul = number1 * number2
    print(f"MUL is {mul}")

  elif choice == 4:
    if number2 == 0:
      print("Cannot Divide")
    else:
      div = number1 / number2
      print(f"DIV is {div}")

  else:
    print("Please choose from 1 - 4")
  


if __name__ == '__main__':
  number1 = int(input("Enter the 1st number : "))
  number2 = int(input("\n Enter the 2nd number : "))
  choice = int(input("Enter your choice .. "))
  print("Press 1 for Add")
  print("Press 2 for Sub")
  print("Press 3 for MUl")
  print("Press 4 for Div")
  calculator(number1,number2)
