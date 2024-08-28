# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

from collections import Counter

class RansomeWord():
  def ranSomeWord(self, ransome, magazine ):
    ranSome_count = Counter(ransome)
    magazine_count = Counter(magazine)

    for char, count in ranSome_count.items():
      if magazine_count[char] < count:
        return False 
    return True
  
object = RansomeWord()
res = object.ranSomeWord("aa", "ab")
print(res)