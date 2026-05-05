# Starter Code: Testing Python Code with pytest
#
# This file contains the functions you will write tests for.
# Do NOT change the function signatures — your tests must work with these.
# Create a separate file called test_functions.py for your tests.


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference of two numbers (a - b)."""
    return a - b


def divide(a, b):
    """Return the result of dividing a by b.

    Raises:
        ValueError: if b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_palindrome(text):
    """Return True if text reads the same forwards and backwards, ignoring case.

    Examples:
        is_palindrome("racecar") -> True
        is_palindrome("hello")   -> False
    """
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
