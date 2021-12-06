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

