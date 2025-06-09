from lib.string_builder import *

def test_adding_nothing():
    sb = StringBuilder()
    size = sb.size()
    output = sb.output()
    assert size == 0
    assert output == ""

def test_adding_one_string():
    sb = StringBuilder()
    sb.add('hello')
    size = sb.size()
    output = sb.output()
    assert size == 5
    assert output == "hello"

def test_adding_two_strings():
    sb = StringBuilder()
    sb.add('hello')
    sb.add(' there!')
    size = sb.size()
    output = sb.output()
    assert size == 12
    assert output == "hello there!"