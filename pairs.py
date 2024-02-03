
arr = [1,2]
print("array =",arr)
def solve(arr):
    i=0
    j=0
    n=len(arr)
    t=[]
    while i<n:
        while j<=i:
            if(i==j):
                t.append((arr[i],arr[j]))
            else:
                t.append((arr[j],arr[i]))
                t.append((arr[i],arr[j]))
            j+=1
        i+=1
        j=0
    return t
    
print("Ans: ",solve(arr))