[TOC]

# Hello World

```javascript

<script>
    console.log("Hello world!")
</script>


```

# Comment

```javascript
// This is a single line comment

/* This is a
multi line comment
*/
```

# Data type and variable

* undefined: a variable that has not been defined
* null
* boolean
* string
* symbol
* number
* object: functions as a library


```javascript
<script>
/* 
comment
*/
console.log("hello");

var myName = "RH" // throughout the whole program
myName = 8 // var is assignable

let outName = "JavaCoding" // recommend to use let
const pi = 3.14 // var that should never change
</script>
```

* decimal number declaring is also possible

# Operators
* remainder: % `11 % 3 = 2`
* a += 1 is also possible

# String
* single quotation, double quotation both possible
* double quote inside the quote: `let str = "String \"Inside the String\" here";`
* single, double quote both can exist. `let str = '<a href="https://instagram.com/" target="_blank">Link</a>';`

# Code output
* \' single quote
* \" double quote
* \\ backslash
* \n newline
* \r carriage return
* \t tab
* \b backspace
* \f form feed

# Concatunate string
* `myStr = "First" + "Second";`
* `myStr = = "Hello" + Name + "hey";`

# Find length of string
```javascript
let myName = "Ramie";
len = myName.length;
```

# bracket notation
```javascript
myName = "Ramie";
a = myName[0];

last = myName[myName.length - 1];
```

# String immutability
* String cannot be altered. individual char cannot be changed.

# Array
```javascript
let arr = ["John", 22];
let arr2 = [];

```

# Nested array
```javascript
let Arr = [["Bulls", 23], ["White fox", 22]]
```

# Modify arr with index
```javascript
let arr = [18,64,99];
arr[1] = 45; // [18,45,99]
```

# Push
* it functions as `append` as in python
```javascript
arr = [1, 2, 3]
arr.push(4, 5) // arr = [1,2,3,4,5]
```

# Pop
* remove from arr (removes only last value) and return the value
```javascript
arr = [1, 2, 3]
arr.pop() // arr = [1,2]
```

# Shift
* remove from arr (removes only from first) and return the value
```javascript
arr = [1, 2, 3]
arr.shift() // arr = [2,3]
```

# Unshift
* append from first
```javascript
arr = [1, 2, 3]
arr.unshift(0) // arr = [0,1,2,3]
```

# Function
```javascript
function test_func(a, b) {
    return a - b;
}

test_func(3, 2);
```

# global scope
```javascript
let var1 = 10;

function func() {
    console.log(var1 + 20);
}
func() // 30
```

# boolean
```javascript
function test_func() {
    return true; // or false
}
```
# if
```javascript
function test(int) {
    if (int) {
        return true;
    }
    return false;
}
```
# triple equal sign(strict equality)
* strict equal sign
```javascript
3 == 3 // True
3 == '3' // True

3 === 3 // True
3 === '3' // False
```

# strict inequality
* strict inequal sign
`if (val !== 17) is also possible`

# logical operator
* `if (val <= 50 && val >= 25)`: here && works as and
* || : pipes work as `or` logical operator

# else if, else
```javascript
if (val > 10) {
    return ""
} else if (val < 5) {
    return
} else {
    return
}
```

# switch
* works as case
```javascript
function test(val) {
    let answer = "";
    switch(val) {
        case 1:
            answer = "alpha";
            break;
        case 2:
            answer = "beta";
            break;
        case 3:
            answer = "gamma";
            break;
        default:
            answer = "other";
            break;
    }
    return answer;
}

function test2(val) {
    let answer2 = "";
    switch(val) {
        case 1:
        case 2:
        case 3:
            answer2 = "low";
            break;
        case 4:
        case 5:
        case 6:
            answer2 = "mid";
            break;
        default:
            answer2 = "high";
            break;
    }
    return answer2;
}
```

# javascript objects
* similar to dictionary
```javascript

let dog = {
    "name": "Bill",
    "tails": 1,
    "friends": ["everything"],
    "the drink": "water",
    1: "age"
};

let name = dog.name; // Bill
let drink = dog["the drink"];

let num = 1;
let age = dog[num]

// if we use dog.name = "Tim", the value changes
dog['bark'] = 'woof!'; // adding property to object
delete dog.bark; // deletes bark
```

# check property
```javascript
let dog = {
    "name": "Bill",
    "tails": 1,
    "friends": ["everything"],
    "the drink": "water",
    1: "age"
};

if (dog.bark) {
    console.log(dog.bark)
} else {
    console.log("not found")
}
```

# multiple objects in a var
```javascript
let dog = {
    "name": "Bill",
    "tails": 1,
    "friends": ["everything"],
    "the drink": "water",
    1: "age"
},

dog2 = {
    "name": "Tim",
    "tails": 1,
    "friends": ["no friends"],
    "the drink": "milk",
    2: "age"
}
```

# nested objects
```javascript
let dog = {
    "name": "Bill",
    "tails": 1,
    "friends": {
        "name": "susan",
        "age": "2",
        "drink": ["juice", "coke"]
    },
    "the drink": "water",
    1: "age"
}
// dog.friends.drink[1] == 'coke'
```

# while loop
```javascript
let arr = [];
let i = 0;
while(i < 5) {
    arr.push(i);
    i++;
}
```

# for loop
```javascript
let arr = [];

for (let i = 0; i < 5; i++) {
    arr.push(i);
}

arr = [1, 3, 6, 10];
let temp = 0;
for (let i = 0; i < arr.length; i++) {
    temp += arr[i];
}
```

# nested for loop
```javascript
let sum = 0;
let num = [[1,2],[3,4],[5,6]]

for (let i=0; i < num.length; i++) {
    for (let j=0; j < num[i].length; j++){
    sum += num[i][j];
    }
}
console.log(sum);

for (var idx in num){
    num[idx].update();
```

# do...while
* exec at least one time and gets into while loop
```javascript
let arr = [];
let i = 6
do {
    arr.push(i);
} while (i < 5)
```

# generate random fraction num
* this cannot be 1 but num between 0 - 1 is generated
```javascript
function random_fraction() {
    return Math.random();
}
console.log(random_fraction())
```

# generate random integer
```javascript
 // with Math.floor()
function random_int() {
    return Math.floor(Math.random() * 10); // floor is rounding down
}
console.log(random_int())
```

# generate random integer within a range
```javascript
function rand_range(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

console.log(rand_range(2,10));
```

# parseInt function
```javascript
function toInt(str) {
    return parseInt(str);
}

// with radix
function toInt(str) {
    return parseInt(str, 2); // set as binary num with number
}
```

# ternary operator(conditional)
```javascript
// condition ? statement-if-true : statement-if-false;

function check(a, b) {
    return a === b ? true : false; // if a ===b, return true
}

// multiple ternary
function checkSign(num) {
    return num > 0 ? "positive" : num < 0 ? "negative" : "zero";
}
console.log(checkSign(1));
```

# var, let, const variables
* let : does not let you declare variable twice(limited in the block)
* var : function scope
* "use strict"; : use strict restrictions

# const(read only)
* variable cannot be redefined
* when const, capitalise the var name
* `const VAR = "const variable";`

# mutate an array declared with const
```javascript
const s = [5,7,2];
function edit_value(s) {
    s[0] = 2;
    s[1] = 5;
    s[2] = 7;
}
```

# prevent object mutation
```javascript
const MATH_CONSTANTS = {
    PI: 3.14
}

Object.freeze(MATH_CONSTANTS)
try {
    MATH_CONSTANTS.PI = 99;
}  catch( ex ) {
    console.log(ex);
}

const PI = freezeObj();
```

# anonymous function
```javascript
// sample
const magic = () => new Date();

// rewrite the function into anonymous function form
let myConcat = function(arr1, arr2) {
    return arr1.concat(arr2);
}

const myConcat = (arr1,arr2) => arr1.concat(arr2);
```

# default parameters
```javascript
const increment = (function() {
    return function increment(number, value = 1) {
        return number + value;
    };
})();
console.log(increment(5,2));
console.log(increment(5));
```

# rest operator
```javascript
const sum = (function() {
    return function sum(...args) { // ... takes anything
        const args = [x,y,z];
        return args.reduce((a,b) => a + b, 0);
    };
})();
console.log(sum(1, 2, 3));
```

# spread operator
```javascript
const arr1 = ['JAN', 'FEB', 'MAR', 'APR', 'MAY'];
let arr2;
(function() {
    arr2 = [...arr1];
    arr1[0] = 'potato'
})();
console.log(arr2); // arr2[0] is not potato. it copies the value, not the address
```

# destructuring assignment
```javascript
let val = {x: 1, y: 3, z: 2};
// old way
let a = val.x;
let b = val.y;
let c = val.z;

// quicker way
const {x: a, y: b, z: c} = val; // get xyz into abc from object val
```

# destructuring assignment with nested object
```javascript
const local_forecast = {
    today: {min: 72, max: 83},
    tomorrow: {min: 73.3, max: 84.6}
};

const {tomorrow: {max: maxOfTomorrow}} = local_forecast; // nested
```

# destructing assignment from array
* it goes into the variables with orders
```javascript
const [z, x, , y] = [1, 2, 3, 4, 5, 6]; // we can skip the order with blank.
// z=1, x=2, y=4
```

# switching values
```javascript
// switching
let a = 8, b = 6;

(() => {
    [a, b] = [b, a]
})();

console.log(a);
console.log(b);
```

# rest operator with array
```javascript
const source = [1,2,3,4,5,6];
function removeTwo(list) {
    const [ , , ...arr] = list; // only first two elements with no value
    return arr;
}
const arr = removeTwo(source);
console.log(source);
console.log(arr); // first two elements removed
```