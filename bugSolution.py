def improved_function_with_error_handling(a, b):
    try:
        # Explicit type checking and conversion
        if not isinstance(a,(int, float)) or not isinstance(b,(int, float)):
            return "TypeError: Operands must be numeric"
        if b == 0:
            return "Division by zero"
        result = a / b
        return result
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Test cases
a = "10"
b = 2
print(improved_function_with_error_handling(a, b)) # Output: TypeError: Operands must be numeric

a = 10
b = 0
print(improved_function_with_error_handling(a, b))  # Output: Division by zero

a = 10
b = 2
print(improved_function_with_error_handling(a, b))  # Output: 5.0

a = 10
b = [1, 2, 3]
print(improved_function_with_error_handling(a, b)) # Output: TypeError: Operands must be numeric

a = None
b = None
print(improved_function_with_error_handling(a, b)) # Output: TypeError: Operands must be numeric