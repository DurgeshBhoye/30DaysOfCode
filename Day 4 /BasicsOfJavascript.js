// Converting a string to a number

const str = "10";
const num = parseInt(str); // num is now 10

// Converting a number to a string

const num = 10;
const str = String(num); // str is now "10"

// Converting a boolean to a number

const bool = true;
const num = Boolean(bool); // num is now 1

// Converting a number to a boolean

const num = 10;
const bool = Boolean(num); // bool is now true

// Converting an object to a string

const obj = { name: "John Doe" };
const str = JSON.stringify(obj); // str is now "{"name":"John Doe"}"

// Converting a string to an object

const str = "{"name":"John Doe"}";
const obj = JSON.parse(str); // obj is now { name: "John Doe" }



// Closures in Javascript:

function outerFunc() {
  let num = 10;

  function innerFunc() {
    return num;
  }

  return innerFunc;
}

const output = outerFunc();
console.log(output()); // 10



// var and const keywords in JS:

// var keyword

var num = 10;
num = 20; // This is allowed

// const keyword

const str = "Hello";
str = "World"; // This will throw an error



// Loops in JavaScript:

// for loop

for (let i = 0; i < 10; i++) {
  console.log(i);
}

// foreach loop

const fruits= ["apple", "mango", "banana", "grapes", "orange"];

fruits.forEach((fruit) => {
  console.log(fruit);
});

// for-of loop

const arr = [1, 2, 3, 4, 5];

for (const num of arr) {
  console.log(num);
}

// for-in loop

const obj = {
  name: "John Doe",
  age: 30,
};

for (const key in obj) {
  console.log(key, obj[key]);
}



// Lexical scope in JavaScript:

let num = 10; // Global scope

function outerFunc() {
  let num = 20; // Local scope of outerFunc

  function innerFunc() {
    let num = 30; // Local scope of innerFunc
    console.log(num); // 30
  }

  innerFunc();
}

outerFunc();
console.log(num); // 10



// map() method in JS:

const arr = [1, 2, 3, 4, 5];

const doubledArr = arr.map((num) => num * 2);

console.log(doubledArr); // [2, 4, 6, 8, 10]





