import pytest

from unitconvert.distance import miles_to_kilometers,kilometers_to_miles

def test_miles_to_kilometers():
    # test conversion from miles to kilometers
    assert miles_to_kilometers(100) == 160.934

def test_kilometers_to_miles():
    # test conversion from kilometers to miles
    assert round(kilometers_to_miles(100),4) == 62.1371
