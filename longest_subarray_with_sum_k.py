def longestSubarrayWithSumK(a: [int], k: int) -> int:
    # Write your code here
    i=0
    j=0
    s = 0
    length = 0
    while j < len(a):
        if s < k:
            s += a[j]
            j += 1
        elif s == k:
            length = max(length,j-i)
            s += a[j]
            j += 1
        else:
            s -= a[i]
            i += 1
    print(i,j)
    while i < len(a) and s > k:
        s -= a[i]
        i += 1
    
    print(i,j)
    if s == k:
        length = max(length,j-i)
    return length

a = "8 15 17 0 11".split()
a = list(map(int,a))
k = 17

print(longestSubarrayWithSumK(a,k))