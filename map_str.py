def solve(s,t):
    d={} 
    
    for i in range(len(s)):
        if s[i] not in d:
            if t[i] not in d.values():
                d[s[i]] = t[i]
            else:
                return False
        elif d[s[i]] != t[i]:
            return False
    return True

s = "add"
t = "egg"
print(solve(s,t))