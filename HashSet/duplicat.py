# Example 1
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

class ContainsDuplicate():
  def containsDuplicate(self, nums):

    duplicate = set()

    for item in nums:
      if item in duplicate:
        return True
      duplicate.add(item)

    return False

object = ContainsDuplicate()
res = object.containsDuplicate(nums = [1,2,3,1])
print(res)