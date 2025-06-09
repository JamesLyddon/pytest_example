import pytest
from lib.present import *

def test_unwrapping_nothing():
    pres = Present()
    with pytest.raises(Exception) as e:
        pres.unwrap()
    error_msg = str(e.value)
    assert error_msg == "No contents have been wrapped."

def test_wrapping_then_unwrapping_something():
    pres = Present()
    pres.wrap('bike')
    present = pres.unwrap()
    assert present == "bike"

def test_wrapping_twice():
    pres = Present()
    pres.wrap('bike')
    with pytest.raises(Exception) as e:
        pres.wrap('skateboard')
    error_msg = str(e.value)
    assert error_msg == "A contents has already been wrapped."