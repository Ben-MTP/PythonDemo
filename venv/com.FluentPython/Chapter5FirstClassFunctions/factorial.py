def factorial(n):
    """
    Function return number factorial of N: int
    :param n:
    :return: factorial(n-1);
    """
    return 1 if n < 2 else n * factorial(n-1);

print(factorial(5));

print(factorial.__doc__)
