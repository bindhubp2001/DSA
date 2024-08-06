def merge_strings(word1, word2):
    merge = ""
    min_length = min(len(word1), len(word2))


    for i in range(min_length):
        merge += word1[i] 
        merge += word2[i]
    
    merge += word1[min_length:] 
    merge += word2[min_length:]

    return merge

result = merge_strings("hello", "wor")
print(result) 