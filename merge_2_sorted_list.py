def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = m - 1  #num1 pointer
    j = n - 1 #num2 pointer
    k = len(nums1) - 1 # Index values to put on 
    
    while i >= 0 and j >= 0:
        if (nums1[i] > nums2[j]):
            nums1[k],nums1[i] = nums1[i],nums1[k]
            i -= 1
            k -= 1
        else:
            nums1[k] = nums2[j] 
            j -= 1
            k -= 1
    
    while j>=0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    print(nums1)
    
    
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

merge(nums1,m,nums2,n)