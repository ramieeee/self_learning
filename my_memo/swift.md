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
```swift
class name {

}
```

# class inheritance
```swift
class Car {
    var topSpeed = 200
    
    func drive() {
        print("driving at \(topspeed)")
    }
}

// future car extends Car class and can use car fields
class Futurecar : Car {
    func fly() {
        print("flying")
    }
}
```

* overriding
```swift
override func drive() {
    print("driving at \(topSpeed + 50)")
}
```

* pointing at original field or field using super
```swift
class Futurecar : Car {
    func fly() {
        super.drive()
        print("flying")
    }
}
```

# initializer
```swift
class Person {
    var name
    var age
 
    // multiple initializer
    init() {
    }
    
    init(name:String, age:Int) {
        self.name = name
        self.age = age
    }
}
```

# optionals
optional is marked with question mark("?")
```swift
class Game {
    var title = ""
}

class Person{
    var name:String? // it could be null or String
    var hobby:Game? // it could be null or have Game type
}
```

* to check if the optional has a value, use optional binding
```swift
let person = Person()
person.name = "ramieeee"

// if there is name, value is saved into actualName
if let actualName = person.name { 
    print(actualName) // ramieeee
}
```

* if we know if the field has a value, use exclamation mark
```swift
if person.name != nil {
    print(person.name!) // unwrapping
}
```

# properties
they are fields as in java

# computed property
class Person

# array
```swift
var d = ["dog", "cat"]

d += ["owl", "mouse"] // appending values
d.remove(at:0) // removing index number 0
d.count // length of array
```

# dictionary
```swift
var db = Dictionary<String, String>() // declare key, value datatype
var db2 = [String:String]() // the same format to declare dictionary

db["student1"] = "ramie" // adding key, value
db["student1"] = nil // removing key, value

for (stdNum, name) in db {
    print(stdNum + name)
}
```
