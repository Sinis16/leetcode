""" Module providing cooking time functions
"""

#Constants
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time depending on layers
    Parameters:
        number_of_layers (int): Number of layers the lasagna has.

    Returns:
        int: Preparation time (in minutes).
    """

    return number_of_layers*PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate preparation time depending on layers
    Parameters:
        number_of_layers (int): Number of layers the lasagna has.
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: elapsed time (in minutes).
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time