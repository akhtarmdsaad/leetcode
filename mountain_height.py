array = [2,1,4,7,3,2,5]
array = [1,2,3,4,5,6,7]
array = [3,2]
array = [0,2,0,2,1,2,3,4,4,1]
array = [875,884,239,731,723,685]
# array = [2,2,2]
def solve(array):
    """
    States : 
        A - going up 
        B - going down
        C - end of mountain
    """
    # INITIALIZE 
    A = "A"
    B = "B"
    C = "C"
    i = 0
    state = A
    count = 0
    max_count = 0
    prev_state = A
    while i < len(array)-1:
        # print(array[i],count,max_count,state)
        if state == A:
            if (array[i] < array[i+1]):
                count += 1
            elif (array[i] == array[i+1]):
                count = 0
                state = C
            elif count > 0:
                state = B
        if state == B:
            if(array[i] > array[i+1]):
                count += 1
                if (i == len(array)-1):
                    state = C
            elif (array[i] == array[i+1]):
                count = 0
                state = C
            else:
                # count = 1
                state = C 
        if state == C:
            if (max_count < count):
                max_count = count
                count = 0
            state = A
        
        i+=1
    # print("Outside loop:",max_count)
    if (max_count < count and state == B):
        max_count = count
    # check last value 
    
    return max_count + 1 if max_count else max_count
    
"""

[875,884,239,731,723,685]
Output
3
Expected
4
"""

max_count = 0
def solve2(array):
    i = 1
    count = 0
    count_list = []
    A = "A: up"
    B = "B: down"
    C = "C: end"
    state = C
    def update_max_count(count):
        global max_count
        if count > max_count:
            max_count = count
        count_list.append(count)
        print("max count updated")
    while i < len(array):
        print()
        print(f"checking {array[i-1]} and {array[i]}:")
        print("\tState:",state,", Count:",count,", Max Count:",max_count)
        if(array[i-1] > array[i]):
            print("down part")
            if (state == A):
                state = B 
                count += 1
            elif count != 0:
                count += 1
        elif(array[i-1] < array[i]):
            print("up part")
            if state == B:
                if count != 0:
                    update_max_count(count)
                    count = 0
                state = A
            elif state == C:
                state = A 
                count = 2
            else:
                count += 1
        else:
            count = 0
            print("no mountains")
            state = C 
        
        if state == C and count != 0:
            update_max_count(count)
            count = 0
        print("To count:",count,"and state:",state)
        i+=1
    print("Last Count We get:",count)
    return max_count,count_list
print("Input:",array)
print("Result:", solve(array))
print("Result:", solve2(array))