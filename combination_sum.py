# combinatories Sum

def solve(array,target):
    t = []
    
    def recurse(array,target,l,i):
        if i==len(array):
            return
        if sum(l)>target:
            return
        elif sum(l) == target:
            t.append(l)
            return
        recurse(array,target,l+[array[i]],i+1)
    
    for i in range(len(array)):
        recurse(array,target,[],i)
    return t

array = [22,3,5,4,6]
target = 10

print(solve(array,target))