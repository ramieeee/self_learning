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

last = myName[myName.length - 1]
```

# String immutability
* String cannot be altered. individual char cannot be changed.