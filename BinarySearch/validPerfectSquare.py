# Example 1:

# Input: num = 16
# Output: true
# Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
# Example 2:

# Input: num = 14
# Output: false
# Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

def isPerfectSquare(num: int) -> bool:
    if num < 1:
        return False
    
    left, right = 1, num

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid 

        if square == num:
            return True
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1
    return False

num = 1
print(isPerfectSquare(num)) # Output: True