s = "HELLO"

stack = []

for char in s:
  stack.append(char)

reversedString = ""

while len(stack) > 0:
  reversedString += stack.pop()

print(reversedString, end="")


