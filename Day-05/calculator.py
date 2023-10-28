import sys
def add(a, b):
    c = a + b
    return c
def sub(a, b):
    c = a - b
    return c
def mul(a, b):
    c = a * b
    return c
def div(a, b):
    c = a % b
    return c
a = float(sys.argv[1]) # by default it gonna read it as a string, that's why we converted to a float, we can make it's a int as well
operation = sys.argv[2]
b = float(sys.argv[3])
if operation == 'add':
    output = add(a, b)
    print(output)
elif operation == 'sub':
    output = sub(a, b)
    print(output)
elif operation == 'mul':
    output = mul(a, b)
    print(output)
elif operation == 'div':
    output = div(a, b)
    print(output)
else:
    print("enter the proper operator")                

