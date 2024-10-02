def add_numbers(a, b):
    sum_value = a + b
    print(sum_value)
add_numbers(4, 6)
sum_stuff = add_numbers(4,4)
print(f"This is the sum_stuff result: ", {sum_stuff})    

print("==============================================")

def add_numbers(a, b):
    sum_value = a + b
    return sum_value
add_numbers(4, 6)
sum_stuff = add_numbers(4,4)
print(f"This is the sum_stuff result: ", {sum_stuff})    