row = 5
col = 5


def isPath(arr):
    path = False
    paths = []
    for index, i in enumerate(arr):
        if i[index] == 0:
            path = True
            paths.append(0)
        else:
            path = False
    if paths != [0, 0, 0, 0, 0]:
        return False
    else:
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
