
    
def solve(arr,k):
    def calc_missing(elem,index):
        return elem-index-1
    
    # check arr[0]
    if calc_missing(arr[0],0) >= k:
        return k 
    
    low = 0
    high = len(arr) - 1
    while low<=high:
        mid = (low+high) // 2
        ck = calc_missing(arr[mid],mid)
        if ck < k and (mid == len(arr) - 1 or calc_missing(arr[mid+1],mid+1)>=k):
            print
            break 
        elif ck < k:
            low = mid + 1
        else:
            high = mid - 1
    # print("mid:",mid)
    return arr[mid]+k-ck
    
    
arr = [1,6]
k = 1
print(solve(arr,k))

# print(calc_missing(2,0))