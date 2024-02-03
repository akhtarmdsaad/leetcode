array = [1,11]

def solve(array):
    dic = {}
    count = 0
    for i in array:
        if i in dic:
            if dic[i] == 0:count += 1
            else:dic[i] -= 1
        else:dic[i] = i-1
    return sum(dic.values()) + count

print(solve(array))