def isSubsequence(s: str, t: str) -> bool:
    i, j = 0, 0
    
    while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
    
    return i == len(s)


s1 = "abc"
t1 = "ahbgdc"
print(isSubsequence(s1, t1))  


s2 = "axc"
t2 = "ahbgdc"
print(isSubsequence(s2, t2))  