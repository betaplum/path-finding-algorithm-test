## How Algorthim Works??
The function gets the next value after the first 0 in the first row and compares it to the previous value and sets the current value equal to the previous value only if it is not equal to -1, then it finds the max between (first-row & first column) & (previous row & the previous column) and sets the current index to that max. If the index value is -1 then there’s no change and if the final index at right bottom is 0 it returns True.

## Big O notation
This algorthim can be improved to be time efficient as it may tend to be slow when the matrix 
magnitude grows and also by creating a single forloop than can include python methods and libs like enumerate and pandas to make the process a little bit faster and less time consuming.