import math
def sqrt(num):
    return math.sqrt(num)
def power(base, exponent):
    return base ** exponent
def log(base, num):
    return math.log(num, base)
def sin(angle):
    return math.sin(angle)
def cos(angle):
    return math.cos(angle)
def tan(angle):
    return math.tan(angle)
def deg_to_rad(degrees):
    return math.radians(degrees)
def rad_to_deg(radians):
    return math.degrees(radians)
def factorial(num):
    return math.factorial(num)
def abs_val(num):
    return abs(num)
def inv(num):
    return 1/num
def percent(num):
    return num/100
def exp(num):
    return math.exp(num)
def get_pi():
    return math.pi
def get_e():
    return math.e
# Prompt the user for what type of calculation they want to perform
calculation = input("What type of calculation would you like to perform? (sqrt, power, log, sin, cos, tan, deg_to_rad, rad_to_deg, factorial, abs_val, inv, percent, exp, get_pi, get_e): ")
# Perform the calculation based on the user's input
if calculation == "sqrt":
    num = float(input("Enter the number: "))
    result = sqrt(num)
    print(f"Square root of {num} is {result}")
elif calculation == "power":
    base = float(input("Enter the base: "))
    exponent = float(input("Enter the exponent: "))
    result = power(base, exponent)
    print(f"{base} to the power of {exponent} is {result}")
elif calculation == "log":
    base = float(input("Enter the base: "))
    num = float(input("Enter the number: "))
    result = log(base, num)
    print(f"Log base {base} of {num} is {result}")
elif calculation == "sin":
    angle = float(input("Enter the angle in degrees: "))
    result = sin(deg_to_rad(angle))
    print(f"Sine of {angle} degrees is {result}")
elif calculation == "cos":
    angle = float(input("Enter the angle in degrees: "))
    result = cos(deg_to_rad(angle))
    print(f"Cosine of {angle} degrees is {result}")
elif calculation == "tan":
    angle = float(input("Enter the angle in degrees: "))
    result = tan(deg_to_rad(angle))
    print(f"Tangent of {angle} degrees is {result}")
elif calculation == "deg_to_rad":
    degrees = float(input("Enter the angle in degrees: "))
    result = deg_to_rad(degrees)
    print(f"{degrees} degrees in radians is {result}")
elif calculation == "rad_to_deg":
    radians = float(input("Enter the angle in radians: "))
    result = rad_to_deg(radians)
    print(f"{radians} radians in degrees is {result}")
elif calculation == "factorial":
    num = int(input("Enter the number: "))
    result = factorial(num)
    print(f"Factorial of {num} is {result}")
elif calculation == "abs_val":
    num = float(input("Enter the number: "))
    result = abs_val(num)
    print(f"Absolute value of {num} is {result}")
elif calculation == "inv":
    num = float(input("Enter the number: "))
    result = inv(num)
    print(f"Inverse of {num} is {result}")
elif calculation == "percent":
    num = float(input("Enter the number: "))
    result = percent(num)