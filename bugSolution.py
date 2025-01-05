def my_function_iterative(x):
    result = 0
    for i in range(1, x + 1):
        result += i
    return result

print(my_function_iterative(5)) # This will work correctly
print(my_function_iterative(1000)) # This will also work correctly