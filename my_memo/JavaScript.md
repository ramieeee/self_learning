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