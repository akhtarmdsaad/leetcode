
def solve(l):
    d = {}
    for i in l:
        x = "".join(sorted(i))
        if x in d:
            d[x] = (*d[x],i)
        else:
            d[x] = (i,)
    
    return [list(i) for i in d.values()]


l = ["eat","tea","tan","ate","nat","bat"]
print(solve(l))