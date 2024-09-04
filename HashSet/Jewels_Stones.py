# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
# Example 2:

# Input: jewels = "z", stones = "ZZ"
# Output: 0

class JewelsStones():
  def jeewl_stones(self, jewels, stones):
    jewel_set = set(jewels)
    count = 0

    for item in stones:
      if item in jewel_set:
        count += 1
    return count
  
jewels = "aA"
stones = "aAAbbbb"

object = JewelsStones()
res = object.jeewl_stones(jewels, stones)

print(res)