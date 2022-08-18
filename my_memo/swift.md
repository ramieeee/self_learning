# variable

use `var` when declaring normal variable
use `let` when declaring constant
```swift
var str:String = "hello world!"
var char:Character = "a"
let num:Int = 21
```

# types
String
Int
Float
Double
Bool


```swift
var a:Int = 10
print(String(c))
```

# if condition

```swift
<!--&&, || could be used-->
if (condition) {
    code
}
else if condition2 {
    code
}
```

# switch statement
```swift
switch value to consider {
case value1:
    respond to value 1
case value2:
    ...
case value3, value4:  <-when we want many cases
    ...
default:
    ...
}
```

# Loop

* for loop
```swift
for i in 1...5 {
    print(i)
}
```

* while loop
```swift
var i:Int = 0
while i < 10 {
    print(i)
    i += 1
}
```

* repeat-while
it is just the same as do-while 
```swift
var i:Int = 0
repeat {
    print("hi")
    i += 1
} while i < 10
```

# function
* without return
```swift
func name() {
    print("hi")
}
```

* with return
```swift
func name() -> DataType {
    someCode
    return someValue
}
```

*example
```swift
func myFunction() -> Int {
    let a:Int = 1
    let b:Int = 2
    
    return a + b
}

print(myFunction()) // 3
```

# function with parameter
* parameter labels are used so it is more of natural English when read
```swift
func add(using num1:Int, and num2:Int) -> Int{
    return num1 + num2
}

add(using:1, and:2)
```

* without labels
```swift
func add(_ num1:Int, _ num2:Int) -> Int{
    return num1 + num2
}

add(2, 2)
```

# class

