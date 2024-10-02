# Function 1: Add two numbers and print the result
def add_numbers(a, b):
    result = a + b
    print(result)  # Print the result directly

# Function 2: Multiply two numbers and print the result
def multiply_numbers(a, b):
    result = a * b
    print(result)  # Print the result directly

# Call the functions
add_numbers(5, 3)          # This will print 8 directly
multiply_numbers(8, 2)     # This will print 16 directly

# Trying to store the result will not work as expected
sum_value = add_numbers(5, 3)         # This will print 8, but sum_value will be None
product_value = multiply_numbers(8, 2) # This will print 16, but product_value will be None

# Output the variables (which will be None)
print("Sum:", sum_value)          # Output will be None
print("Product:", product_value)  # Output will be None


# How print works in this example:
# add_numbers(5, 3) prints 8 directly, but it does not return anything. Therefore, sum_value will be None.
# multiply_numbers(8, 2) prints 16 directly, but similarly, product_value will be None.
# When we try to print sum_value and product_value, they will both be None because the functions don’t return values.
# Key Differences:
# With return: The function returns the result, which can be stored and reused. You have more flexibility to use the values.
# With print: The function directly prints the result, but you cannot store or reuse the value in the calling code. Any attempt to store the result will lead to None.