# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed. 

# Example 1:

# Input: text = "nlaebolko"
# Output: 1
# Example 2:

# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:

# Input: text = "leetcode"
# Output: 0

class Solution(object):
    def maxNumberOfBalloons(self, text):
      ballon_set = {'b', 'a', 'l', 'o', 'n'}
      freq = {}
      for char in text:
          if char in ballon_set:
              if char in freq:
                freq[char] +=1
              else:
                freq[char] = 1
      for char in  ballon_set:
         if char not in freq:
            freq[char] = 0
      return min(freq['b'], freq['a'], freq['l']//2, freq['o']//2, freq['n']) 
        
object = Solution()
print(object.maxNumberOfBalloons("loonbalxballpoon")) # 2    