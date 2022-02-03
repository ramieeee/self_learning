[toc]

# Java

* JVM: Java Virtual Machine
* JRE: Java Runtime Environment
* IDE to be used: Eclipse



## making a project

* in the project directory: src -> package -> class



# Main

Java runs in object-oriented way. It needs classes to be executed.

```java
// basic code from eclipse
package tutorial;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
}
```

# Print

* `System.out.println("text");` would be the basic syntax to print text out

```java
package tutorial;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Hello World!");
		System.out.println("Hello World! 2");
	}
}
```

# Data type and variable

* int, double, boolean, char, String

```java
package tutorial;

public class Main {
	public static void main(String[] args) {
		// primitive (not changable)
		int hello_world = 5;
		double num2 = 5.0;
		boolean b = true;
		char c = 't'; // single quotation mark
		
		// String is a different data type
		String str = "this is string"; // double quotation mark
	}
}
```

# operation

All operation is the same as other languages except division

```java
package tutorial;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int x = 5;
		int y = 7;
		int z = 57;
		int u = z * y + x - y;
		System.out.println(u);
	}
}
```

# Division

* if one of the operands is double, the output is always double data type

```java
package tutorial;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int x = 5;
		int y = 7;
         int m = 25 % 3; // modulus or remainder operation
		double z = 57;
		double u = z / y;
		System.out.println(u);
	}
}
```

# Exponent

```java
// exponent is a double data type
int x = 5;
int y = 7;

// '**' doesn't apply to Java
double n = Math.pow(x, y);
```

# Type casting

* instead of changing data type when initializing, we could change the type of the value

```java
int x = 5;
int y = 7;
int z = 57;
double u = x / (double)y;
```

# Input

```java
package tutorial;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		String scanned = sc.next();
		int scanned = sc.nextInt(); // if I want it to be int
		boolean scanned = sc.nextBoolean(); // if I want it to be boolean
		double scanned = sc.nextDouble(); // if I want it to be double
		System.out.println(scanned);
	}
}
```

* take input as string, and convert into int

```java
Scanner sc = new Scanner(System.in);
String scanned = sc.next();
int x = Integer.parseInt(scanned);
```

# Comparison operator

* and: &&
* or: ||
* not: !. it is the reversing the value

```java
// String comparison
Scanner sc = new Scanner(System.in);
String s = sc.next();
s.equals("hello"); // it is not s == "hello";
```

# if, else, else if

```java
package tutorial;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();
		
		if (s.equals("helloworld")) {
			System.out.println("helloworld!");
		}
		else if (s.equals("hello")) {
			System.out.println("hey");
		}
		else {
			System.out.println("other");
		}
	}
}
```

# Array

* To declare an array, put the type that I want it to be

```java
public class Main {

	public static void main(String[] args) {
		String[] newArr = new String[5];
		newArr[0] = "hello"; 
		newArr[1] = "hi";
		newArr[2] = "tim";
		newArr[3] = "bill";
		newArr[4] = "joe";
		
		int[] nums = {2, 3, 45, 6, 1};
		double[] nums2 = {2.1, 3.8};
		
		int x = nums[4];
		System.out.println(x);
	}
}
```

# For loop

```java
public class Main {
	public static void main(String[] args) {
		int[] arr = {1,5,7,3,4,5};
		for (int i = 0; i < arr.length; i++) {
			if (arr[i] == 5) {
				System.out.println("Found a 5 at index " + i);
			}			
		}
	}
}
// for loop could be
// (int i = 0; i < arr.length; i+=5) meaning, 5 will be added to i for every loop
```

# For each loop

* just like `for element in arr:` in python

```java
public class Main {
	public static void main(String[] args) {
		int[] arr = {1,5,7,3,4,5};		
		int count = 0;
        
        // just like `for element in arr:` in python
		for (int element:arr) {
			System.out.println(element + " " + count);
			count++;
		}
	}
}
```



```java
public class Main {
	public static void main(String[] args) {
		String[] names = new String[5];
		Scanner sc = new Scanner(System.in);
		
		for (int i = 0; i < names.length; i++) {
			System.out.print("Input: ");
			String input = sc.nextLine();
			names[i] = input;
		}
		
		for (String n:names) {
			System.out.println(n);
		}
	}
}
```

# break

```java
for (String n:names) {
	System.out.println(n);
	if (n.equals("tim")) {
		break;
	}
}
```

# While

* It is exactly the same as for loop

```java
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Type a number: ");
		int x = sc.nextInt();
		
		int count = 0;
		while (x != 10) {
			System.out.println("Type 10...");
			System.out.print("Type a number: ");
			x = sc.nextInt();
			count++;
		}
		System.out.println("You tried " + count + " times");
	}
}
```

# Do while

* program operates `do` first and checks `while`

```java
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int x;
		
		do {
			System.out.print("Type a number: ");
			x = sc.nextInt();
		} while (x != 10);
	}
}
```

# Sets and list

* Set: collection of unordered elements that are unique. element cannot be contained twice.
* Set is very fast compared to list.

```java
package tutorial;
import java.util.Set;
import java.util.HashSet;

public class Main {
	public static void main(String[] args) {
		// HashSet is a standard set
		Set<Integer> t = new HashSet<Integer>();
		t.add(5);
		t.add(5); // adding another 5 does not do anything as 5 already exists
		t.add(9);
		t.remove(9); // removing the element 
		t.isEmpty(); // checks if set is empty
		t.size(); // checks size
		System.out.println(t);
		
		// to check if set contains 5
		boolean x = t.contains(5);
		System.out.println(x);
	}
}
```

* TreeSet: it comes with an order

```java
import java.util.TreeSet;

Set<Integer> t = new TreeSet<Integer>();
```

* LinkedHashSet

```java
import java.util.LinkedHashSet;

Set<Integer> t = new LinkedHashSet<Integer>();
```

* List: it wors the same as array but slower. It can add things and remove elements

```java
import java.util.ArrayList;

public class Main {
	public static void main(String[] args) {
		// HashSet is a standard set
		ArrayList<Integer> t = new ArrayList<Integer>();
		t.add(1);
		t.add(2);
		t.add(3);
		t.add(4);
		
		t.get(0); // get a value of index 0. it is not t[0]
		t.set(0, 5); // changing the value of the index 0th to 5
		t.size();
		t.subList(0, 2); // get values in the range of 0 - 1
		System.out.println(t.subList(0, 2));
	}
}
```

* LinkedList: faster in some operation

```java
import java.util.LinkedList;

LinkedList<Integer> t = new LinkedList<Integer>();
```

# Maps and HashMaps

* It is like dictionary in python
* key and value pair(list or array)
* very fast
* HashMap does not guarantee orders. It is only extremely fast like `set`

```java
import java.util.Map;

public class Main {
	public static void main(String[] args) {
		Map m = new HashMap();
		m.put("key", "value"); // putting key and value in the map
		m.put("joe",  5);
        
		System.out.println(m); // output as {key=value}
		System.out.println(m.get("key")); // to get value of "key"
         System.out.println(m.values()); // prints all values of m

         m.claer(); // to empty the Map
         m.isEmpty(); // tells if m is empty
	}
}
```

* TreeMap(): the key has to be in the same type. it sort the keys in orders.

```java
import java.util.TreeMap;

public class Main {
	public static void main(String[] args) {

		Map m = new TreeMap();
		m.put("key", "value");
		m.put("joe",  5);
		
		System.out.println(m);
		System.out.println(m.get("key"));
	}
}
```

* LinkedHashMap(): It keeps the order the user puts in.



# Practice 1

* Counting all letters in the string

```java
public class Main {
	public static void main(String[] args) {
		Map m = new HashMap();
		String str = "hello my name is Ramie";
		
        // str.toCharArray() converts the string into an array
		for(char x:str.toCharArray()) {
			if (m.containsKey(x)){
				int old = (int) m.get(x);
				m.put(x,  old+1);
			}
			else {
				m.put(x,  1);
			}
		}
		System.out.println(m);
	}
}
```

# Sorting

```java
public class Main {
	public static void main(String[] args) {
		int[] x = {-99, 5, 1, 2, 5, 7};
		
		// sorting array
		Arrays.sort(x);
		
		for(int i:x) {
			System.out.print(i + ",");			
		}
	}
}
```

# Objective oriented programme

* object: instance of data type
* method: a method comes with an instance like length method in `var.length();`

```java
// calling functions within the Main class
public class Main {
	public static void main(String[] args) {
		System.out.println(add2(1));
		System.out.println(str("Hi"));
	}
	
	public static int add2(int x) {
		return x + 2; 
	}
	
	public static String str(String x) {
		return x + "!";
	}
}
```

# Creating classes

* When creating classes, we need to make a file for the class
* class is like a Data type
* attribute: variable that holds information

```java
// Dog.java
package tutorial;

public class Dog {
	private String name; // an attribute
	private int age;
	
	public Dog(String name, int age) { // dog object
		this.name = name; // instance
		this.age = age;
	}
	
	public void speak() {
		System.out.println("I am " + this.name + " and I am " + (this.age));
	}
}
```

```java
// Main.java
package tutorial;

public class Main {
	public static void main(String[] args) {
		Dog tim = new Dog("Tim", 4);
		tim.speak();
	}
}
```



# Subclasses

* Make another class called Cat, and we could reuse Dog class's methods

```java
package tutorial;

public class Cat extends Dog {
	private int food;
    
	// Cat is the subclass(child class)	
	public Cat(String name, int age, int food) {
		super(name, age);
		this.food = food;
	}
	
	// another way to set up the method
	public Cat(String name, int age) {
		super(name, age);
	}
	
	// hard code "0" or other numbers
	public Cat(String name) {
		super(name, 0);
	}

    // overwrite speak method only for Cat class
	public void speak() {
		System.out.println("Meow my name is " + this.name + " and I get fed" + this.food);
	}
}
```

* Then Dog and Cat classes could be called to main function

```java
package tutorial;

public class Main {
	public static void main(String[] args) {
		Dog tim = new Dog("tim", 18);
		tim.speak();
		
		Cat bob = new Cat("bob");
		bob.speak();
	}
}
```

# Static Variable

* It works as a class variable that could be called for every methods within the class.

// class Dog

```java
package tutorial;

public class Dog {
	public String name;
	public int age;
	protected static int count = 0;
	
	public Dog(String name, int age) { // dog object
		this.name = name;
		this.age = age;
		Dog.count += 1;
	}
}
```

// Main

```java
package tutorial;

public class Main {
	public static void main(String[] args) {
		Dog tim = new Dog("tim", 9);
		Dog bill = new Dog("bill", 5);
		System.out.println(Dog.count); // value is 2
	}
}
```

# Static Method

* it works as a function in other languages
* It does not care about instance but it just does something

```java
	public static void display() {
		System.out.println("I am a dog!");
	}
```

# Compare objects

* if there was no boolean equals method in Student class, it will compare addresses and returns false.

```java
package tutorial;

public class Main {
	public static void main(String[] args) {
		Student Joe = new Student("Joe");
		Student Bill = new Student("Joe");
		
		System.out.println(Joe.equals(Bill)); // returns true
         System.out.println(Joe.compareTo(Tim)); // returns -10 (a number)
	}
}
```

```java
package tutorial;

public class Student {
	private String name;
	
	public Student(String name) {
		this.name = name;
	}
	
	public boolean equals(Student other) {
		if (this.name == other.name)
			return true;
		else {
			return false;
		}
	}
    // Comparing bigger, smaller
    public int compareTo(Student other) {
		return this.name.compareTo(other.name);
	}
    
    public String toString() {
		return "Student(" + this.name + ")"; // returns Student(Tim), not address
	}
}
```

# Inner Classes

* OuterClass class

```java
package tutorial;

public class OuterClass {
	public void Inner() {
		class InnerClass {
			public void display() {
				System.out.println("Inner Class");
			}
		}
		
		InnerClass in = new InnerClass();
		in.display();
	}
}
```

* Main class

```java
package tutorial;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		OuterClass out = new OuterClass();
        out.Inner();
       
        System.out.println();
	}
}
```

