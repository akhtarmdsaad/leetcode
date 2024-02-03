# 3sum closest
import time,random

def solve(array,target):
    array.sort()
    min_sum = float("inf")
    min_sum_tuple = ()
    for i,a in enumerate(array):
        if i>0 and a == array[i-1]:
            continue 
        l = i+1
        r = len(array) - 1
        while l<r:
            s = a + array[l] + array[r]
            if abs(s-target) < min_sum:
                min_sum = abs(s-target)
                min_sum_tuple = (array[i],array[l],array[r])
            if s>target:
                r -= 1
                while l<r and array[r]==array[r+1]:
                    r -= 1
            elif s<target:
                l+=1
                while l<r and array[l]==array[l-1]:
                    l+=1
            else:
                return (array[i],array[l],array[r])
            
    return min_sum_tuple
def brute_force(array,target):
    minsum=float("inf")
    to_ret = ()
    x = range(len(array))
    for i in x:
        for j in x:
            for k in x:
                if i!=j and i!=k and j!=k:
                    s = array[i]+array[j]+array[k]
                    diff = abs(target-s)
                    if diff < minsum:
                        diff = minsum 
                        to_ret = (array[i],array[j],array[k])
    return to_ret


array = [15485,1548,545,14,48,21,5,746,1,56,46,31,65,6,11,64,31,6,4,3,146,3,22,84512,641,5146,35,4,54,4,845,1548,531,31,684351,84512,531,214,52,1,46,3215,46,315,645,15,461,2,351,34,1,385,1,6385,153,64835,641,4315,634,51,43,13451,6,3415,6,351,64,4351]
target = 90000
print("Generating...",end="\r")
for i in range(random.randint(1500,9900)):
    array.append(random.randint(0,5412045))

i = random.randint(0,len(array))
j = random.randint(0,len(array))
while j == i:
    j = random.randint(0,len(array))
k =  random.randint(0,len(array))
while k==i or k==j:
    k = random.randint(0,len(array))
array.sort()
i = len(array)-1
j = i-1 
k = j-1
target = array[i] + array[j] + array[k] + random.randint(1,54)
print(len(array),target,"\n",array[i],array[j],array[k])
print("Generated")
# Find a triplet that sums to target(or near target)
# print(sorted(array),target)
st = time.time()
print(solve(array,target))
print("Time taken by algo:",time.time()-st)
st=time.time()
print(brute_force(array,target))
print("Time taken by brute force:",time.time()-st)