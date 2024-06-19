with open('currencyData.txt') as f:
  readFile = f.readlines()

print(readFile)

currencyDict = {}
for line in readFile:
  parsed = line.split("\t")
  currencyDict[parsed[0]] = parsed[1]

print(currencyDict)
amount = int(input("Enter the amount : \n"))

print("enter name of the you want to convert this amount to? Availability Options:\n")
[print(item) for item in currencyDict.keys()]

currency = input("Please enter one of these values")
print(f'{amount} INR is equal to {amount * float(currencyDict[currency])} {currency}')
