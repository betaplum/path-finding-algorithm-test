# How algorithm works
- Basically the goal is to change all 0s in the grid into 1s through iterative array transversal
- Start with first element in the grid arr[0][0], change it a 1
- And then procced to convert all 0s into 1s in the first row
- Repeat for process for first column in the grid, but now difference if you refence values of corresponding cells in first row
- For the remaining cells in the grid, to assign value to current 0 cell you compare value of preceeding cell column wise to the value of the precceding cell row wise and return the largest number of the two.

# How to improve algorithm (Big O Notation)
The current algorithm has a Big O notaion of On^2, to improve it I would consider using a _set_ or _map_ data structure to persist cell values and evaluate them instead of nested _for loops_.