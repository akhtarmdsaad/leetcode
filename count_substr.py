from typing import *

def countSubStrings(s: str, k: int) -> int:
    # Write your code here
    
    def count_char(s,k):
        return len(set(s)) == k
    
    i = 0
    sum = 0
    while i < len(s):
        j = i
        while j <= len(s):
            cs = s[i:j]
            if count_char(cs,k):
                sum += 1
            j += 1
        i += 1
    print("Sum is :",sum)
    return sum


s = "aacfssa"
k = 3
print(countSubStrings(s,k))