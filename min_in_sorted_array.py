def findMin(nums) -> int:
    l = 0
    r = len(nums) - 1
    
    #check 0 rotation
    if nums[0] <= nums[-1]:
        return nums[0]
    
    while l<=r:
        mid = (l+r) // 2
        print(l,mid,r,nums[mid])
        if nums[mid] < nums[0]:
            print("Entered less than part")
            if 0 < mid < len(nums)-1 and nums[mid-1] > nums[mid] < nums[mid+1]:
                return nums[mid]
            else:
                r = mid - 1 
        else:
            print("Entered else part")
            if 0 < mid < len(nums)-1 and nums[mid-1] > nums[mid] < nums[mid+1]:
                return nums[mid]
            else:
                l = mid + 1
    return nums[l]

array = [
    [3,4,5,1],
    [3,1,2],
    [1]
]
for arr in array:
    print(arr)
    print("Ans:",findMin(arr))
    print()