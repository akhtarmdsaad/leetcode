no = 324


def solve(no):
    # binary search 
    l = 1
    u = no 
    m = (l+u) // 2
    while not (m**2 <= no and (m+1)**2 > no):
        if m**2 < no :
            l = m 
        elif m**2 > no:
            u = m
        m = (l+u) // 2
    return m

print("Result:",solve(no))