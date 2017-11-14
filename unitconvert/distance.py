"""
This module contains functions to convert between miles and km.
@ Ty Janoski
11/14/17
"""
def miles_to_kilometers(dm):
    """
    Convert distance in miles to kilometers.

    PARAMETERS
    ----------
    dm : float
        The distance in miles.

    RETURNS
    -------
    dk : float
        The distance in kilometers.
    """
    return dm*1.60934
def kilometers_to_miles(dk):
    """
    Convert distance in kilometers to miles.

    PARAMETERS
    ----------
    dk : float
        The distance in kilometers.

    RETURNS
    -------
    dm : float
        The distance in miles.
    """
    return dk*0.621371

