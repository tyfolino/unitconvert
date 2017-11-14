"""
This module will convert temperatures from C to F and F to C.
@Ty Janoski
11/14/17
"""

def fahrenheit_to_celcius(TF):
    """
    Convert temperature in Fahrenheit to Celcius.

    PARAMETERS
    ----------
    TF : float
        The temperature in degrees Fahrenheit.

    RETURNS
    -------
    TC : float
        The temperature in degrees Celcius.
    """

    return (TF - 32)*(5/9)

def celcius_to_fahrenheit(TC):
    """
    Convert temperature in Celcius to Fahrenheit.

    PARAMETERS
    ----------
    TC : float
        The temperature in degrees Celcius.

    RETURNS
    -------
    TF : float
        The temperature in degrees Fahrenheit.
    """
    return (TC * (9/5)) + 32
