# Path Finding Algorithm Test

This test should take no longer than 20 mins max.

## Objective

Given a 2D array(m x n) the task is to check if there is any path from top left to bottom right.
In the matrix, 1 is considered as blockage (can’t go through this cell) and 0 is considered as the path cell (can go through it).

Note: Top left cell will always contain a 0

```
Input : arr[][] = {{ 0, 0,  0, -1,  0 },
                  { -1, 0,  0, -1, -1 },
                  {  0, 0,  0, -1,  0 },
                  { -1, 0,  0,  0,  0 },
                  {  0, 0, -1,  0,  0 }}
Output : Yes

Input : arr[][] = {{ 0, 0,  0, -1,  0 },
                  { -1, 0,  0, -1, -1 },
                  {  0, 0,  0, -1,  0 },
                  { -1, 0, -1,  0,  0 },
                  {  0, 0, -1,  0,  0 }}
Output : No
````
