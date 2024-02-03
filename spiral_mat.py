import math

def solve(mat):
    t = []
    state = "right"
    m = len(mat)
    n = len(mat[0])
    i,j = 0,0
    x,y = math.ceil((m+1)/2),math.ceil((n+1)/2)
    count = 0
    while True:
        elem = mat[i][j]
        print(elem,end=" ")
        if state == "right":
            if i >= m-1:
                i = m-1
                state = "down"
                continue
            i+=1
        elif state == "down":
            if j >= n-1:
                j = n-1 
                state = "left"
                continue
            j += 1
        elif state == "left":
            if i <= 0:
                i = 0
                state = "up"
                continue
            i -= 1
        elif state == "up":
            if j <= 0:
                j = 0
                state = "right"
                continue 
            j -= 1
        input(state)

mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(solve(mat))