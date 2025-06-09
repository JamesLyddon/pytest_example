from lib.counter import *

def test_no_adding_returns_0_msg():
    counter = Counter()
    result = counter.report()
    assert result == "Counted to 0 so far."

def test_adding_twice_returns_correct_count():
    counter = Counter()
    counter.add(10)
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 15 so far."