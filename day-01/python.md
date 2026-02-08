## What is Python?

Python is a high-level, interpreted programming language ideal for DevOps and automation tasks. Its simple, readable syntax enables quick scripting for infrastructure management, CI/CD pipelines, configuration management, and monitoring. Python supports multiple paradigms (procedural, object-oriented, functional) and has extensive libraries for cloud integration, containerization, and system administration.

## Python Interpreter
- Background: Written in C language
- Executes code top-down

## Program vs Script

| Program | Script |
|---------|--------|
| Complex logic code | Set of instructions |
| Compiled | Interpreted |

## Variables and Constants

### Variables
- **Definition**: Vary + able (can change)
- **Example**: `env = 'dev'`
- Variables store values that can be modified during execution

### Constants
- Fixed values that don't change
- **Example**: `dev` (configuration value)

## Data Types

| Type | Examples |
|------|----------|
| `int` | 1, 3, 56, 7000 |
| `float` | 1.2, 5.655 |
| `bool` | True, False |
| `string` | "this is string" |

## Naming Conventions

Python uses **snake_case**:
- **Correct**: `hello_world.py`
- **Avoid**: `helloWorld.py` (camelCase)

## Type Casting
Convert input to required data type should use where required like at taking input:

```python
a = int(input("Enter the number: "))
```


## Loop
#for
for i in range(5):


for - type of loop
i - variable
range - (start, stop, increament/decrement)



#while
while varible = "a":
    print("print something")


## function

def func_name()
    function steps

func_name() #function calling
