import string
import random

if __name__ == "__main__":
  s1 = string.ascii_uppercase
  s2 = string.ascii_lowercase
  s3 = string.digits
  s4 = string.punctuation

  passwordLength = int(input("Enter You PassWord Length : "))

  password = []

  password.extend(list(s1))
  password.extend(list(s2))
  password.extend(list(s3))
  password.extend(list(s4))

  random.shuffle(password)

  print("".join(password[0:passwordLength])) #method 1

  print("".join(random.sample(password,passwordLength))) # method 2

