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

