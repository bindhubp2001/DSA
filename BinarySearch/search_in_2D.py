# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        m,n = len(matrix), len(matrix[0]) # to get number of rows and columns in matrix
        left, right = 0, m*n - 1 # initialize binary search pointers

        # Binary Search Loop
        while left <= right:
          mid = (left + right) // 2

          mid_value = matrix[mid // n][mid % n]

          if mid_value == target:
              return True

          elif mid_value < target:
              left = mid + 1
          
          else:
              right = mid - 1
          
        return False

            
    
obj = Solution()
result = obj.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)
print(result)