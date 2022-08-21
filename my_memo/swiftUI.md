# Views

# Text
* modifiers
padding()

# Image
* modifiers
resizable()
aspectRatio(contentMode: .fit) // fitting size

# VStack, HStack, ZStact
* virtically, horizentally, overly stacking views
* we can give spacing

# Spacer()
* take all available spaces

# Button
* closer
```swift
Button("text", action: {
    print("hello")
})
```

* trailing closure
```swift
Button("text") {
    print("hello")
}
```

* label view
```swift
Button(action: {
    print("hello")
}, label: {
    HStack {
        Image(systemName: "pencil")
        Text("Edit")
    }
})
```
* sf symbols have free icons to download 

# State
* state properties are the same as react state
```swift
@state private var card = "card1" // initial state value

card = "card2" // change state
```
