import pytest
from lib.report_length import *

def test_5_char_word():
    result = report_length('12345')
    assert result == 'This string was 5 characters long.'

def test_empty_str():
    result = report_length('')
    assert result == 'This string was 0 characters long.'

def test_int_for_str():
    with pytest.raises(TypeError):
        report_length(5)