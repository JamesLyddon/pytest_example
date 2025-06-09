import pytest
from lib.password_checker import *

def test_valid_password():
    pc = PasswordChecker()
    valid = pc.check('12345678')
    assert valid

def test_invalid_password():
    pc = PasswordChecker()
    with pytest.raises(Exception) as e:
        pc.check('1234567')
    msg = str(e.value)
    assert msg == "Invalid password, must be 8+ characters."