# version_control
Get familiar with version control basics

## Description
A simple math library that includes a division and addition function. The division function includes a division by zero check. The repo also includes a script which tests the library with a few basic commands.

## How to use
You can use this library by simply importing it into your Python file and then using it as any other library:

```
import math_lib

add_result = math_lib.add(2, 3)
div_result = math_lib.div(2, 3)
```

Included in the repo is a testing script to check the library. Run this with the command:

```
python calculate.py
```

Also included is a convenience script to test using sh:

```
chmod +x run.sh
./run.sh
```

Running either of these commands should lead to the below output:

```
Testing division (3 / 2): 1.5
Testing division (3 / 0): None
Testing addition (3 + 2): 5
```


## How to install
Simply clone the repo locally and make sure to have Python installed.