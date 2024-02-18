
def calc_m(arr,days,k):
    "returns no of bouqets that can be made"
    s = ""
    for i in arr:
        if i > days:
            s += "_"
        else:
            s += "x"
        # print(i,days)
    return s.count("x"*k)
    

def solve(arr,k,m):
    
    l = 0
    h = 2**31
    
    while l<=h:
        mid = (l+h) // 2
        c_m = calc_m(arr,mid,k)
        elif c_m > mid:
            h = mid - 1 
        else:
            l = mid + 1
    return -1




arr = [1542,5142,4695,4385,2629,2492,933,1068,151,3960,3790,1196,3842,5147,5526,5528,2259,1708,2714,5462,3016,3262,1175,4348,4826,80,789,5285,3855,3455,3480]
m = 49
k = 4
print(solve(arr,k,m))
