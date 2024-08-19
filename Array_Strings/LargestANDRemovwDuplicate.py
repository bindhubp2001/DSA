arr = [22,4,5,67,7,7,89,0]


def Largest(arr):
  max = arr[0]
  for i in range(len(arr)):
    if arr[i] > max:
      max = arr[i]
  return max



def removeDuplicate(arr):
  duplicate = 0

  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      if arr[i] == arr[j]:
        duplicate = arr[i]
        print("Duplicate Element : ",duplicate)
        arr.remove(duplicate)
        return arr
  return arr



print("Array after removing duplicate element : ",removeDuplicate(arr))
print("Largest Element in Array : ",Largest(arr))
    


