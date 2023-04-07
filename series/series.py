def fibonacci(n) :
    """
    Return the nth number in the fibonacci sequence.
    argumenst:
        n (integer): The index of the number in the sequence.
    Returns:
         integer: The nth number in the fibonacci sequence.
    """
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def lucas(n) :
    """
    Return the nth number in the lucas sequence.
    arguments:
        n (integer): The index of the number in the sequence.
    Returns:
         integer: The nth number in the lucas sequence.
    """
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n-1) + lucas(n-2)


def sum_series(n, first1=0, second2=1) :
    """
    Calling this function with no optional parameters will produce numbers from the fibonacci series. Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers.
    arguments:
        n (integer): The index of the number in the sequence.
        first (integer, optional): The first number in the sequence. Defaults to 0.
        second (integer, optional): The second number in the sequence. Defaults to 1.
    Returns:
        integer: The nth number in the sequence.    
    """
    if n == 0:
        return first1
    if n == 1:
        return second2
    return sum_series(n-1, first1, second2) + sum_series(n-2, first1, second2)
