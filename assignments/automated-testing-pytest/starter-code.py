def add(first_number, second_number):
    """Return the sum of two numbers."""
    return first_number + second_number


def is_even(number):
    """Return whether a number is even."""
    return number % 2 == 0


def divide(dividend, divisor):
    """Divide two numbers, rejecting a zero divisor."""
    if divisor == 0:
        raise ValueError("divisor must not be zero")
    return dividend / divisor