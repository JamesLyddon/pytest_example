from lib.check_codeword import *

def test_correct_guess():
    """
    If the guess is correct ('horse')
    Returns:
    str: "Correct! Come in."
    """
    result = check_codeword('horse')
    assert result == "Correct! Come in."

def test_close_guess():
    """
    If the guess is not 'horse' but starts with 'h' and ends with 'e'
    Returns:
    str: "Close, but nope."
    """
    result = check_codeword('hose')
    assert result == "Close, but nope."

def test_wrong_guess():
    """
    If the guess is wrong
    Returns:
    str: "WRONG!"
    """
    result = check_codeword('sheep')
    assert result == "WRONG!"