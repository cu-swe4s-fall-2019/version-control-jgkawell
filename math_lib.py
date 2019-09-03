def div(a, b):
    """
    Divides two inputs (checks for division by zero) 
    
    Parameters
    ----------
    a (double): The numerator for the division
    b (double): The denominator for the division

    Returns
    ----------
    d (double): The result of the division
    
    """
    if b == 0:
        # cannot divide by zero
        return None
    else:
        return a / b


def add(a, b):
    """
    Adds two numeric inputs
    
    Parameters
    ----------
    a (double): The first number to sum
    b (double): The second number to sum

    Returns
    ----------
    d (double): The result of the summation
    
    """
    return a + b
