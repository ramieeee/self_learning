

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

```

```

