# No of Pallindrome in string

def check_pal(string,index):
    i = index
    j = index 
    while i>=0 and j < len(string):
        if string[i] == string[j]:
            i -= 1
            j += 1
    
    i = index
    j = index + 1
    while i>=0 and j < len(string):
        if string[i] == string[j]:
            i -= 1
            j += 1
     
    return 
    

def solve(s):
    i = 0
    while i < len(s):
        ch = s[i]
        # is ch pallindrome
        check_pal(s,i)

s = "Hello Man"
print(solve(s))
