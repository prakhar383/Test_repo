def divide(a, b):
    """Returns the quotient of a and b. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
