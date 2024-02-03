# 3 SUM

def solve(array):
    array.sort()
    t = []
    for i,a in enumerate(array):
        if i>0 and a==array[i-1]:
            continue
        
        l = i + 1
        r = len(array)-1
        
        while l<r:
            if a+array[l]+array[r] > 0:
                r -= 1
            elif a+array[l]+array[r] < 0:
                l += 1
            else:
                t.append([a,array[l],array[r]])
                l += 1
                while l<r and array[l] == array[l-1]:
                    l += 1
        
    return t
    

array = [0,0,0,0]
print(solve(array))