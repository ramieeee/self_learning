Typescript

- extension to javascript
- to avoid runtime error
- needs transfiled to javascript as browser cannot read it

# install

`npm install -g typescript`

# execute

- write typescript file such as main.ts
- and transfile using `tsc main.ts' command
- and main.js file will be created
- `tsc main.ts -w` , with watching option, will show errors

# ts config

- indicate rootDir, outDir and transfile all tsfiles in rootDir `tsc -w`

# grammar

- variable cannot be changed to other type once initialized
- but always state type explicitely like `let hello: string = "world";`

# function

```javascript
// always specify parameter type and return type
const getName = (name: string, surname: string): string => {
  return name + " " + surname;
};
```

# create object

```javascript
const user: { name: string, age: number } = {
  // meaning this user object should have name and age property
  name: "ramie",
  age: 30,
};
```

# interface

- special entity that helps object type reduce codes\*

```javascript
// Starts with capital
interface UserInterface {
  name: string;
  age: number;
}

// no error
const user: UserInterface = {
  name: "ramie",
  age: 30,
};

// causes error because User interface obliges user2 object to have name and age property
const user2: UserInterface = {
  name: "jack",
};
```

# question mark

```javscript
interface UserInterface {
    name: string;
    age?: number; // question mark indicates it is not mendatory
}

// causes no error
const user2: UserInterface = {
    name: "jack",
}
```

# functions inside interface

```javascript
interface UserInterface {
  name: string;
  age?: number;
  getMessage(): string; // return is string type
}

const user: UserInterface = {
  name: "ramie",
  age: 30,
  getMessage() {
    return "Hello";
  },
};

console.log(user.getMessage()); // Hello
```

# Union

- we can give many types to properties

```javascript
interface UserInterface {
  name: string;
  surname: string;
}

// several data types in a single property
let user: UserInterface | null = null;
```

# type aliases

- it enables users to read and understand quick

```javascript
type ID = string;

interface UserInterface {
  // instead of string. easy to recognize what it is
  id: ID;
  name: string;
  surname: string;
}

type PopularTag = string;
type MaybePopularTag = PopularTag | null; // when we are not sure

// instead of string[]
const PopularTags: PopularTag[] = ["dragon"];
const dragonsTag: MaybePopularTag = null;
```

# void in typescript

- when we don't return anything
- void is `undefined` and `null`

```javascript
const doSomething = (): void => {
  console.log("do something");
};
```

# any in typescript

- worst type in typescript
- typescript is like skipping property if type is any

# never type

- unlikely to use often
- throwing errors

```javascript
const doSomething = (): never => {
  throw "never";
};
```

# unknown type

- can replace any type
- we cannot directly asign unknown type to other variables

```javascript
let vAny: any = 10;
let vUnknown: unknown = 10;

let s1: string = vAny;
let s2: string = vUnknown; // error
```

# type assersion

```javascript
let vUnknown: unknown = 10;
let s2: string = vUnknown as string; // becomes string

let pageNum: string = '1';
let numPageNum: number = pageNum as unknown as number; // becomes number
```

# working with DOM

- element is the highest class in hierarchy

```javascript
const someElement = document.querySelector('.foo');

someElement.addEventListener('blur', (event)=>{
    const target = event.target as HTMLInputElement;
    console.log('event', target.value);
})
```

# classes

- private, protected, public can be utilized

```javascript
interface UserInterface {
    getFullName(): string;
}

class User implements UserInterface{
    // by default everything is public
    private firstName: string;
    private lastName: string;
    readonly unchangableName: string;
    static readonly maxAge = 50;


    constructor(firstName: string, lastName: string) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.unchangableName = firstName;
    }

    getFullName(): string {
        return this.firstName + ' ' + this.lastName;
    }
}

// class extension
class Admin extends User {
    private editor: string;

    setEditor(editor: string): void {
        this.editor = editor;
    }

    getEditor(): string {
        return this.editor;
    }
}

const user = new User("hello", "world");
console.log(user.getFullName()) // hello world
console.log(User.maxAge); // 50

const admin = new Admin('Foo', 'Bar');
console.log(admin.getFullName()) // Foo Bar

admin.setEditor("edit here");
console.log(admin.getEditor()); // edit here
```

# generics

```javascript
// we don't know which object.
// so we write <T> generic
const addId = <T extends object>(obj: T) => { // T should be an object
    const id = Math.random().toString(16);
    return {
        ...obj,
        id: id,
    }
}

interface UserInterface<T, V> {
    name: string;
    data: T;
    meta: V;
}

const user: UserInterface<{meta: string}, string> = {
    name: "Jack",
    data: {
        meta: "foo"
    },
    meta: "bar"
}

const user2: UserInterface<String[], string> = {
    name: 'john',
    data: ['foo', 'bar', 'baz'],
    meta: "foo"
}
```

# enums

- simple object
- use it as datatype and value
- by default enums have values like index

```javascript
// with capital letter
enum StatusEnum {
    NotStarted="notStarted",
    InProgress="inProgress",
    Done="done"
}

let notStartedStatus: StatusEnum = StatusEnum.NotStarted;
notStartedStatus = StatusEnum.Done;

// enum usage
interface Tast {
    id: string;
    status: StatusEnum; // only enum is allowed here
}


```
