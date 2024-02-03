# SEarch in rotated array
# Find O(logn) Soln 
import time

def solve(array,n):
    """
    Check first val
    then mid val 
    
    """
    
    low = 0  
    high = len(array) - 1  
    
    while low<high:  
        mid = (low+high) // 2
        if array[mid] == n:
            return mid 
        
        # right part 
        if array[mid] < n:
            if n <= array[high]:
                low = mid + 1
            
        elif n < array[mid]:    
            if array[low] <= n:
                high = mid - 1
        
        print(mid)
    return -1  
  


array = [4,5,6,7,0]
target = 0
print(solve(array,target))