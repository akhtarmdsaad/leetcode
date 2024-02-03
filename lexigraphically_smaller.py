
# [1,2,5,4,3] --> [1,2,5,4,(3)] --> [1,3,2,5,4] --> [1,3,2,4,5] --------} 
# [1,2,5,4,3,5,6] --> [1,2,5,4,3,6,5]
# [1,2,5,4,2] --> [2,1,2,4,5]

array = [1,2,5,4,3]
# array = [1,2,3]
def deprecated(array):
    i=len(array) - 1
    j=len(array) - 1
    last_elem = array.pop()
    while i > 0:
        if(last_elem > array[i-1]):
            # time to exchange
            # last elem to i-1 pos
            # sorted(array[i:])
            # return array[:i] + sorted(array[i:])
            break 
        else:
            i -= 1
    # globals()["array"] = array[:i-1] + [last_elem] + sorted(array[i-1:])
    return array[:i-1] + [last_elem] + sorted(array[i-1:])
    return array

def solve(array):
    # print("-"*15)
    # print("From solve : ")
    i = len(array) - 1
    while i>=0 and array[i]<= array[i-1]:
        i -= 1
    # print(i,array[i])
    j = len(array) - 1
    while i>0 and j > i  and array[j] <= array[i-1]:
        j -= 1
    # print(j,array[j])
    # swap them 
    if i>0:
        array[j],array[i-1] = array[i-1],array[j]
    array[i:] = sorted(array[i:])

array = [4,3,2,1]
print("Input:",array)
# print("Deprecated:",deprecated(array.copy()))
solve(array)
print("Result:",array)


"""
Input:
[1,2,3]
[3,2,1]
[1,1,5]
Output
[1,2]
[3,2]
[1,1]
Expected
[1,3,2]
[1,2,3]
[1,5,1]
"""