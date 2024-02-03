l = [0,0,1,1,1,1,2,3,3]

def solve(l):
    d={}
    parse_index = 0
    replace_index = 0
    while parse_index < len(l):
        elem = l[parse_index]
        if elem in d:
            if (d[elem] < 2):
                d[elem] += 1
                # replace it
                if(replace_index < parse_index):
                    l[replace_index],l[parse_index] = l[parse_index],l[replace_index]
                replace_index += 1
                parse_index += 1
            else:
                # dont replace, the elem is not reqd, move away 
                parse_index += 1
                
        else:
            d[elem] = 1
            if(replace_index < parse_index):
                    l[replace_index],l[parse_index] = l[parse_index],l[replace_index]
            replace_index += 1
            parse_index += 1
    
    return l,replace_index
        

print(solve(l))