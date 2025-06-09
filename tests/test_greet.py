from lib.greet import *

def test_greet_returns_greeting_for_jim():
    greeting = greet('Jim')
    assert greeting == 'Hello, Jim!'