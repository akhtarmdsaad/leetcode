l = [1,3,-1,-3,5,3,6,7]
k = 3

def solve(l,k):
    start_index = 0
    end_index = start_index + k
    t = []
    # 1st get max 
    max_index = -1
    max_val = float("-inf")
        
    # add it to t:list 
    
    # now start sliding the window
    while end_index <= len(l):
        print("Checking:",l[start_index:end_index])
        print("Start Index:",start_index,", Max Index:",max_index,"\n")
        if (start_index > max_index):
            print("IF Branch")
            max_index = start_index
            max_val = l[max_index]
            for i in range(start_index, end_index):
                print("i in for:",i)
                if max_val < l[i]:
                    max_index = i
                    max_val = l[max_index]
        else:
            print("ELSE Branch")
            if (max_val <= l[end_index-1]):
                max_index = end_index-1
                max_val = l[max_index]
            else:
                pass 
        print("Checking:",l[start_index:end_index],end=" Max:")
        print(max_val)
        t.append(max_val)
        start_index += 1
        end_index += 1
    return t
    
print(l)
print("T:",solve(l,k))