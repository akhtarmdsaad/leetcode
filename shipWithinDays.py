



def shipWithinDays(weights, days: int) -> int:
    def checkcap(weights,days,capacity):
        count = 0
        cap2 = 0
        for i in weights:
            cap2 += i
            if cap2 > capacity:
                cap2 = i
                count += 1
        count += 1 if cap2>0 else 0
        return count
    low = 0
    high = sum(weights)
    while low<=high:
        mid = (low+high) // 2
        if checkcap(weights,days,mid) <= mid:
            ans = mid 
            high = mid - 1
        else:
            low = mid + 1
    return ans
    

weights = [1,2,3,1,1]
days = 4
capacity = 3    
print(checkcap(weights,days,capacity))