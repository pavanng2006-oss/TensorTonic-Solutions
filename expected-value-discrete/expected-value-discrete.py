import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    sum = 0
    for xi, pi in zip(x, p):
        sum += xi * pi

    return float(sum)