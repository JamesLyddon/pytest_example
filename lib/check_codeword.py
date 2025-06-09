def check_codeword(codeword):
    """
    Check user entered correct codeword ('horse')
    
    Parameters:
    codeword (str): The user's guess
    
    Returns:
    str: feedback on the user's guess
    """
    if codeword == "horse":
        return "Correct! Come in."
    elif codeword[0] == "h" and codeword[-1] == "e":
        return "Close, but nope."
    else:
        return "WRONG!"