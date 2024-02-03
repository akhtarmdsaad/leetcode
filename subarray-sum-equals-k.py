# 3 SUM

def solve(nums,k):
    i = 0
    j = 0
    s = 0
    count = 0
    while j < len(nums):
        if s < k:
            s += nums[j]
            j+=1
        elif s == k:
            if j - i > 0:
                print("Inc Count, where j-1=",j-i)
                count += 1
            s -= nums[i]
            i += 1
        else:
            s -= nums[i]
            i += 1
        print("i:",i,"j:",j,"Sum:",s,"Count:",count)
    while s>k and i<j:
        s -= nums[i]
        i += 1
    print("i:",i,"j:",j,"Sum:",s,"Count:",count)
    if s == k and j-i>0:
        count += 1  
    return count

array = [1]
k = 3
print(array)
print(solve(array,k))