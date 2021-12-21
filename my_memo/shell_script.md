

[toc]

# Command

* read: Input the data from the user into the variable

```shell
#!bin/sh

echo "What is your name?"
read PERSON
echo "Hello, $PERSON"
```

# Variable

## Local variable

* within the current instance of the shell

## Environment variable

* available to any child process of the shell

## 

```shell
#!/bin/sh

# variable
NAME="Ramie"
readonly NAME # var NAME is fixed and not changable
unset NAME # it cleans the var

```

# Special variables

```shell
$0 # file name of the script
$1...9 # shows the parameter in the position designated
$# # number of argument supplied to the script
$* # all arguments double quoted
$@ # arguments individually quoted
$? # exit status of the last command executed
$$ # process number of the current shell

```

# Basic operators

* arithmetic
* relational
* boolean
* string
* file test operators

# Loops

* while

```shell
#!/bin/sh
# printing 0-9
a=0
while [ $a -lt 10 ]
do
	echo $a
	a='expr $a + 1'
done
```

* for

```shell
#!/bin/sh

# printing 0-9 hard coding
for var in 0 1 2 3 4 5 6 7 8 9
do
	echo $var
done
```

* until

```shell
#!/bin/sh

# printing 0-9
until [ ! $a -lt 10 ]
do
	echo $a
	a='expr $a + 1'
done
```

* nested

```shell
#!/bin/sh


```

* loop control(break)

```shell
#!/bin/sh

a=0

while [ $a -lt 10 ]
do
	echo $a
	if [ $a -eq 5 ]
	then
		break # or continue to keep the program running
	fi
	a='expr $a + 1'
done
```

# Function

```shell
#/bin/sh

#functions

Hello(){
        echo "Hello $1!"
}

# function calling
Hello ramie

Add(){
        return $(expr $1 + $2)
}

Add 3 5
# data saving into var
ret=$?

echo $ret
```

