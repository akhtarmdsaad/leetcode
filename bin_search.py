# Binary search
def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1
    
def solve(arr,target):
    index = binary_search(arr,0,len(arr)-1,x)
    i = index 
    j = index 
    while i>0 and arr[i-1] == arr[index]:
        i -= 1 
    while j<len(arr)-1 and arr[j+1] == arr[index]:
        j += 1
    return (i,j)

arr = [5,7,7,8,8,8,10] 
x = 8

print(solve(arr,x))