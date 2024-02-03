string = "BBABAA"

def solve(string):
    n = len(string)
    i=0
    j=n-1
    count = 0
    while i<j:
        if string[i] == "B":
            count += 1
        if string[j] == "A":
            count += 1
        i+=1
        j-=1
    return count

print(solve(string))
