string = "PAYPALISHIRING"
# string="a"
n = 0

def solve(string,n):
    l = len(string) 
    t = ""
    if n == 1:
        return string
    for row_number in range(n):
        last_index = None
        i = row_number
        while True:
            if i >= l:
                break 
            else:
                if i != last_index:
                    t += (string[i])
                    last_index = i
            i += (n-row_number-1)*2
            if i >= l:
                break 
            else:
                if i != last_index:
                    t += (string[i])
                    last_index = i
            i += row_number*2
    return t
for n in range(5):
    print(solve(string,n))

""