const row = 5;
const col = 5;

const isPath = (arr) => {
  // Please write your code here

  return true;
};

// Test data
const arr = [
  [0, 0, 0, -1, 0],
  [0, 0, 0, -1, -1],
  [0, 0, 0, -1, 0],
  [-1, 0, -1, 0, -1],
  [0, 0, -1, 0, 0],
];

// Main test
if (isPath(arr)) {
  console.log("Yes");
} else {
  console.log("No");
}
