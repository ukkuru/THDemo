def add(a, b):
    """Function to add two numbers."""
    return a + b

def subtract(a, b):
    """Function to subtract two numbers."""
    return a - b

def multiply(a, b):
    """Function to multiply two numbers."""
    return a * b

def divide(a, b):
    """Function to divide two numbers."""
    if b == 0:
        return "Division by zero error"
    return a / b

# Example usage of the functions
print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))
