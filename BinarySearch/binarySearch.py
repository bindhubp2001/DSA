def search(target,nums):
  low = 0;
  high = len(nums)-1


  while low <= high:
    mid = (low + high) // 2
    if nums[mid] == target:
      return mid
    if nums[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return -1

print(search(nums=[4,5,6,2],target=6))

