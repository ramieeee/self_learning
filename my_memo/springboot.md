# Spring Boot

# Download Spring boot
* from Spring Initializr
 - Spring Web
 - Spring Data JPA
 - Spring Data JDBC
 - PostgreSQL Driver
* java version more than 8 required

# configuration
* DemoApplication is where you run springboot
* pom.xml is where all configuraing happens
* Tomcat will run the server at 8080 port

# Basic spring code to run the server
```java
package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@SpringBootApplication
@RestController // it makes the codes below a REST server
public class DemoApplication {

	public static void main(String[] args) {
		SpringApplication.run(DemoApplication.class, args);
	}

	@GetMapping // get method
	public List<String> hello() {
		return List.of("Hello, World");
	}
}

```