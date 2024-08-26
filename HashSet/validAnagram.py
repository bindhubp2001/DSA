# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

class ValidAnagram():
  def validAnagram(self, s, t):
    count_s = {}
    count_t = {}

    if len(s) != len(t):
      return False
    
    for char in s:
      if char in count_s:
        count_s[char] +=1
      else:
        count_s[char] = 1

    for char in t:
      if char in count_t:
        count_t[char] +=1
      else:
        count_t[char] = 1

    return count_s == count_t
  
object = ValidAnagram()
res = object.validAnagram(s = "rat", t="car")
print(res)