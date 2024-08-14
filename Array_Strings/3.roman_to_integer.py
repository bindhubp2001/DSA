def roman_to_integer(s):
    # Step 1: Create a mapping of Roman numerals to integers
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0  
    length = len(s)  
    
    
    for i in range(length):
        
        current_value = roman_map[s[i]]
        
        if i < length - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
            total -= current_value  
        else:
            total += current_value
              

    return total  


print(roman_to_integer("III"))      
print(roman_to_integer("LVIII"))    
print(roman_to_integer("MCMXCIV"))  
