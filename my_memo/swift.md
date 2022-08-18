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
