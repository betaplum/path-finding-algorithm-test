# Finding Path Algorithm

## How Algorithm Works

This algorithm iterates through each inner array and checks the 0th element in the first array and the `n`th element in each consecutive array where `n` is the inner array's index position in the larger array. On each iteration a check is made to see if the `n`th element is equal to 0 or not. A counter is updated each time `array[n]` is not a blockage.

## How to improve algorithm

This algorithm has O(N) complexity. I am not sure what the best way to improve it is. One thought is since the top-left cell will always contain zero, it would improve the performance of this algorithm if the check started on the second array.
