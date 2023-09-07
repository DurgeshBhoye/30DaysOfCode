
const arr = [10, 2, 5, 3, 1];

// Sort the array in ascending order.
array.sort();

console.log(array); // [1, 2, 3, 5, 10]

// Sort the array in descending order.
array.sort(function(a, b) {
  return b - a;
});

console.log(array); // [10, 5, 3, 2, 1]
