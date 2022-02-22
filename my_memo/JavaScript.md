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