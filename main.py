row = 5
col = 5


def isPath(arr):
    
    for i in range(1, len(arr)): 
        if (arr[i][0] != -1): 
            arr[i][0] = arr[i-1][0]
        if (arr[0][i] != -1): 
            arr[0][i] = arr[0][i-1]
   
    for r in range(1, row): 
        for c in range(1, col): 
            if (arr[r][c] != -1): 
                arr[r][c] = max(arr[r][c - 1],  arr[r - 1][c])
                
    
    if arr[row - 1][col - 1] == 0:
        return True

arr = [[0, 0, 0, -1, 0],
       [0,0,0,0,0],
       [-1, -1, 0, 0, 0],
       [0,0,0,-1,-1],
       [0, 0, 0, 0, 0]]

# Main test
if (isPath(arr)):
    print("Yes")
else:
    print("No")
