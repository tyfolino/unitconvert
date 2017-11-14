import pytest

from unitconvert.temperature import fahrenheit_to_celcius,celcius_to_fahrenheit

def test_fahrenheit_to_celcius():
    # test conversion from miles to kilometers
    assert round(fahrenheit_to_celcius(50),1) == 10.0

def test_celcius_to_fahrenheit():
    # test conversion from kilometers to miles
    assert round(celcius_to_fahrenheit(20),1) == 68.0
