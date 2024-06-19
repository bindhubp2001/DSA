#calculate a factorial og give number: 4! = 4*3*2*1
#find trilaing zeros

def factorial(number):
  if(number == 0 or number == 1):
    return 1
  
  else:
    return number*factorial(number-1)


def factorialTrialZeros(number):
  fact = factorial(number)
  print(fact)

  count = 0
  while(fact % 10 == 0):
    count = count + 1
    fact = fact / 10
  return count

if __name__ == '__main__':
  # number = int(input("Enter number...\n"))
  # factorial = factorial(number)
  # print(factorial)
  
  print(factorialTrialZeros(560))