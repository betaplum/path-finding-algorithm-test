row = 5
col = 5


def isPath(arr):
    for index, i in enumerate(arr):
        if i[index] != 0:
            return False
    return True

# Test data
arr = [[0, 0, 0, -1, 0],
       [0, 0, 0, -1, -1],
       [0, 0, 0, -1, 0],
       [-1, 0, -1, 0, -1],
       [0, 0, -1, 0, 0]]

# Main test
if (isPath(arr)):
    print("Yes")
else:
    print("No")
