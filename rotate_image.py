# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]
def print_mat(mat):
    print()
    for i in mat:
        for j in i:
            print(str(j).ljust(2),end=" ")
        print()
def solve(matrix):
    i = 0
    j = 0
    n = len(matrix)
    main_pos = [0,0]
    prev_pos = (0,0)
    curr_pos = (0,0)
    while main_pos[0] <= n // 2:
        x = n - main_pos[0]
        while main_pos[1] < x-1:
            curr_pos = (prev_pos[1],n - prev_pos[0] - 1)
            matrix[main_pos[0]][main_pos[1]],matrix[curr_pos[0]][curr_pos[1]] = matrix[curr_pos[0]][curr_pos[1]] , matrix[main_pos[0]][main_pos[1]]
            prev_pos = curr_pos
            if tuple(prev_pos) == tuple(main_pos):
                main_pos[1] += 1
                prev_pos = main_pos
        main_pos[0] += 1
        main_pos[1] = n-x+1
    
            
print_mat(matrix)
solve(matrix)

print("To Final Result:")
print_mat(matrix)


