def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Type error"

# Uncommon error scenario: a is a string, b is an integer
a = "10"
b = 2
result = function_with_uncommon_error(a, b)
print(result)  # Output: Type error

# Uncommon error scenario: a is an integer, b is a list
a = 10
b = [1, 2, 3]
result = function_with_uncommon_error(a, b)
print(result) # Output: TypeError

# Uncommon error scenario: both a and b are None
a = None
b = None
result = function_with_uncommon_error(a,b)
print(result) # Output: TypeError