def longest_common_prefix(strs):

  min_length = min(len(s) for s in strs)
  
  common_prefix = ""

  for i in range(min_length):
    char = strs[0][i]

    for s in strs[1:]:
      if s[i] != char:
        return common_prefix
      
    common_prefix += char
  return common_prefix

print(longest_common_prefix(["flow","flower","flight"]))

