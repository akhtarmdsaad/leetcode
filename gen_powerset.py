x = [1,2,3]
p = [(1,),(2,),(3,),(1,2),(1,3),(2,3),(1,2,3)]
def recurse(a,elem):
    t=[]
    main_counter = 0
    counters = [0 for i in range(elem)]
    j=len(counters)-1
    i=j
    k=j
    while counters[0] != len(a) and i>=0:
        container=[]
        for _ in counters:
            container.append(x[_])
            print(x[_],end=" ")
        t.append(container)
        print()
        main_counter += 1
        counters[i] += 1
        if (counters[i] == len(a)) and i!=0:
            print("here")
            while counters[i] >= len(a)-1 and i>0:
                i-=1
            counters[i] += 1
            for _ in range(i+1,len(counters)):
                counters[_] = 0
            i = j
    return t
       
def recurse2(a,elem):
    t=[]
    main_counter = 0
    if elem == 1:
        for i in a:
            t.append((i,))
        return t
    counters = [elem for i in range(elem)]
    j=len(counters)-1
    i=j
    k=j
    while counters[0] != len(a)-1 and i>=0:
        container=[]
        for _ in counters:
            container.append(x[_])
            print(x[_],end=" ")
        t.append(tuple(container))
        print()
        main_counter += 1
        counters[i] += 1
        k=i
        if (counters[i] == len(a)) and i!=0:
            print("here")
            while counters[i] >= len(a)-1 and i>0:
                i-=1
            counters[i] += 1
            for _ in range(i+1,len(counters)):
                counters[_] = 0
            i = j
    return t
    
def powerset(x):
    p = [(),tuple(x)]
    
    for i in range(1,len(x)):
        p.extend(recurse2(x,i))
        
    return sorted(p,key=lambda x:len(x))
for i in (powerset(x)):
    print(i)