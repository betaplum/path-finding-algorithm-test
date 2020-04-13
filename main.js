const row = 5;
const col = 5;

const isPath = (arr) => {
 arr[0][0] = 1; 
  
 for (let i = 1; i < row; i++)  
     if (arr[i][0] != -1) 
         arr[i][0] = arr[i - 1][0];    

 for (let j = 1; j < col; j++)  
     if (arr[0][j] != -1) 
         arr[0][j] = arr[0][j - 1];     

 for (let i = 1; i < row; i++)  
     for (let j = 1; j < col; j++)  
       if (arr[i][j] != -1) 
           arr[i][j] = Math.max(arr[i][j - 1], 
                         arr[i - 1][j]);        
   
 return (arr[row - 1][col - 1] === 1)
};

const arr = [
  [0, 0, 0, -1, 0],
  [0, 0, 0, -1, -1],
  [0, 0, 0, -1, 0],
  [-1,0, -1, 0, -1],
  [0, 0, -1, 0, 0],
];

if (isPath(arr)) {
  console.log("Yes");
} else {
  console.log("No");
}
