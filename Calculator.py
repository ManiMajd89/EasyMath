import math
def sum (x,y):
    return x+y

def subtract (x,y):
    return x-y

def multiply (x,y):
    return x*y

def divide (x,y):
    return x/y

def nth_power (x,y):
    return x**y

def square (x):
    return x**2

def cube (x):
    return x**3

def plus_minus (x):
    if x>0:
        return -x
    else:
        return x

def ten_power (x):
    return 10**x

def inverse (x):
    return 1/x

def square_root (x):
    return math.sqrt(x)

def cube_root (x):
    return x **(1/3)

def nth_root (x,y):
    return x ** (1/y)

def factorial (x):
    multiple = 1
    while x > 1:
        multiple *= x
        x -= 1
    return multiple

def sin (x):
    return math.sin(x)

def cos (x):
    return math.cos(x)

def tan (x):
    return math.tan(x)

def csc (x):
    return 1/(math.sin(x))

def sec (x):
    return 1/(math.cos(x))

def cot (x):
    return 1/(math.tan(x))

def log_10 (x):
    return math.log10(x)

list = ["sum", "subtract", "multiply", "divide", "square", "cube", "nth_power", "plus/minus", "power of 10",
            "inverse", "square root", "cube root", "nth root", "factorial", "sin", "cos", "tan", "csc", "sec", "cot",
            "log_10"]

answer = input("If you would like to continue, type 'yes' or 'no': ")

while answer == 'yes':
    print(list)
    num_1 = float(input("Enter a number: "))
    operator = input("Please select one of the operators above: ")
    if operator == "square":
        print(square(num_1))
    elif operator == "cube":
        print(cube(num_1))
    elif operator == "power of 10":
        print(ten_power(num_1))
    elif operator == "inverse":
        print(inverse(num_1))
    elif operator == "square root":
        print(square_root(num_1))
    elif operator == "cube root":
        print(cube_root(num_1))
    elif operator == "factorial":
        print(factorial(num_1))
    elif operator == "log_10":
        print(log_10(num_1))
    elif operator == "plus/minus":
        print(plus_minus(num_1))
    elif operator == "sin":
        print(sin(num_1))
    elif operator == "cos":
        print(cos(num_1))
    elif operator == "tan":
        print(tan(num_1))
    elif operator == "csc":
        print(csc(num_1))
    elif operator == "sec":
        print(sec(num_1))
    elif operator == "cot":
        print(cot(num_1))

    else:
        num_2 = float(input("Enter another number: "))
        if operator == "sum":
            print(sum(num_1, num_2))
        elif operator == "subtract":
            print(subtract(num_1, num_2))
        elif operator == "multiply":
            print(multiply(num_1, num_2))
        elif operator == "divide":
            print(divide(num_1, num_2))
        elif operator == "nth root":
            print(nth_root(num_1,num_2))
        elif operator == "nth_power":
            print(nth_power(num_1,num_2))

    answer = input("If you would like to continue, type 'yes' or 'no': ")






