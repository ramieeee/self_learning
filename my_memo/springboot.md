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

# making a student class
* create a package at com.example.demo directory named `student`
```java
// Student.java
package com.example.demo.student;

import java.time.LocalDate;

public class Student {
    private Long id;
    private String name;
    private String email;
    private LocalDate dob;

    public Student() {
    }

    public Student(Long id, String name, String email, LocalDate dob) {
        this.id = id;
        this.name = name;
        this.email = email;
        this.dob = dob;
    }

    public Student(String name, String email, LocalDate dob) {
        this.name = name;
        this.email = email;
        this.dob = dob;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public LocalDate getDob() {
        return dob;
    }

    public void setDob(LocalDate dob) {
        this.dob = dob;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    @Override
    public String toString() {
        return "Student{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", email='" + email + '\'' +
                ", dob=" + dob +
                ", age=" + age +
                '}';
    }
}

// DemoApplication.java
package com.example.demo;

import com.example.demo.student.Student;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.time.LocalDate;
import java.time.Month;
import java.util.List;

@SpringBootApplication
@RestController
public class DemoApplication {

	public static void main(String[] args) {
		SpringApplication.run(DemoApplication.class, args);
	}

	@GetMapping
	public List<Student> hello() {
		return List.of(
				new Student(
						1L,
						"Ramie",
						"Ramie@gmail.com",
						LocalDate.of(2000, Month.JANUARY, 5),
						21
				)
		);
	}
}

```

# Database connection
* application.properties file lets us to access the database
```java
// sample application.properties
spring.datasource.url=jdbc:postgresql://localhost:5432/student
spring.datasource.username=
spring.datasource.password=
spring.jpa.hibernate.ddl-auto=create-drop
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.PostgreSQLDialect
spring.jpa.properties.hibernate.format_sql=true
```
```SQL
CREATE DATABASE student;
GRANT ALL PRIVILEGES ON DATABASE "student" TO postgres;
```
* After creating DB, make sure to uncomment DB dependencies on pom.xml
* Spring-boot-data-jpa will connect to the DB server
* also connect to postgresql or any other DB from intellij

# Data into DB
* If the code below is run, data will be put into DB
```java
// StudentConfig.java
package com.example.demo.student;

import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.time.LocalDate;
import java.time.Month;
import java.util.List;

import static java.util.Calendar.JANUARY;

@Configuration
public class StudentConfig {

    @Bean
    CommandLineRunner commandLineRunner(
            StudentRepository repository) {
        return args -> {
            Student ramie = new Student(
                    "Ramie",
                    "ramie@gamil.com",
                    LocalDate.of(2000, Month.JANUARY, 5),
            );

            Student deniz = new Student(
                    "Deniz",
                    "deniz@gamil.com",
                    LocalDate.of(2000, Month.JANUARY, 5),
            );

            repository.saveAll(
                    List.of(ramie, deniz)
            );
        };
    }
}

```

# Post request
```java
// StudentRepository.java

// responsible for data access
@Repository
public interface StudentRepository
        extends JpaRepository<Student, Long> { // Student class with Long type id

    // SELECT * FROM student WHERE email = ?
    @Query("SELECT s FROM Student s WHERE s.email = ?1")
    // email check
    Optional<Student> findStudentByEmail(String email);
}
```
```java
// StudentService.java

@Service
public class StudentService {

    // Add student with no email duplication
    public void addNewStudent(Student student) {
        Optional<Student> studentOptional = studentRepository.findStudentByEmail(student.getEmail());
        if (studentOptional.isPresent()) {
            throw new IllegalStateException("email already exists");
        }
        studentRepository.save(student);
    }
}
```
```java
//StudentController.java
public class StudentController {
    @PostMapping
    public void registerNewStudent(@RequestBody Student student) {
        studentService.addNewStudent(student);
    }
}
```

* to get the error message in HTTP response
```java
//application.properties
server.error.include-message=always
```

# DELETE request to DB

```java
// StudentController.java
@DeleteMapping(path = "{studentId}")
public void deleteStudent(@PathVariable("studentId") Long studentId) {
    studentService.deleteStudent(studentId);
}

// StudentService.java
public void deleteStudent(Long studentId) {
    boolean exists = studentRepository.existsById(studentId);
    if (!exists) {
        throw new IllegalStateException("student id " + studentId + " does not exist");
    }
    studentRepository.deleteById(studentId);
}
```