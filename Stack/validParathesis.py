# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

class ValidParenthesis:

    def validParanthese(self,s):
      stack = []
      map = {")": "(", "}": "{", "]": "["}

      for char in s:
        if char in map:
            top = stack.pop() if stack else '#'
            if map[char]  != top:
               return False
        else:
            stack.append(char)
      return not stack
          
    
object = ValidParenthesis()
s = "()[]{}"
res = object.validParanthese(s)

print(res)


          
