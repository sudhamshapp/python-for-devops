# Function 1: Add two numbers and return the result
def add_numbers(a, b):
    result = a + b
    return result  # Return the result to the caller

# Function 2: Multiply two numbers and return the result
def multiply_numbers(a, b):
    result = a * b
    return result  # Return the result to the caller

# Call the functions and use their return values
sum_value = add_numbers(5, 3)
product_value = multiply_numbers(sum_value, 2)

# Output the results
print("Sum:", sum_value)           # Output will be 8
print("Product:", product_value)   # Output will be 16


# How return works in this example:
# add_numbers(5, 3) returns the sum 8, which is stored in sum_value.
# multiply_numbers(sum_value, 2) uses sum_value and multiplies it by 2, returning 16, which is stored in product_value.
# Both results are printed using print after the function calls.
