def solve(nums):
    # get counts 
    i = 0
    counts = {
              "0":0,
              "1":0,
              "2":0
             }
    while i<len(nums):
        if nums[i] == 0:
            counts["0"] += 1
        elif nums[i] == 1:
            counts["1"]+=1
        elif nums[i] == 2:
            counts["2"] += 1
        i+=1
    
    zero_index = 0
    one_index = counts["0"]
    two_index = counts["0"] + counts["1"]
    print(zero_index,one_index,two_index)
    i = 0
    while i < len(nums):
        print(nums,i,nums[i])
        if nums[i] == 0:
            if i > zero_index:
                nums[i],nums[zero_index] = nums[zero_index],nums[i]
                print("Swapped indexes:",i,zero_index)
                i -= 1
            zero_index += 1
        if nums[i] == 1:
            if i >= counts["0"] + counts["1"] or i < counts["0"]:
                nums[i],nums[one_index] = nums[one_index],nums[i]
                print("Swapped indexes:",i,one_index)
                i -= 1
            one_index += 1
        if nums[i] == 2:
            if i < (counts["0"] + counts["1"]):
                nums[i],nums[two_index] = nums[two_index],nums[i]
                print("Swapped indexes:",i,two_index)
                i -= 1
            two_index += 1
        i+=1
        
    return nums
nums = [0,2,1]
print(solve(nums))

print("Nums is:",nums)