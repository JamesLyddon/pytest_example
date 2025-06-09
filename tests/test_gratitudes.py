from lib.gratitudes import *

def test_no_items():
    grats = Gratitudes()
    result = grats.format()
    assert result == "Be grateful for: "

def test_single_item():
    grats = Gratitudes()
    grats.add('puppies')
    result = grats.format()
    assert result == "Be grateful for: puppies"

def test_two_items():
    grats = Gratitudes()
    grats.add('puppies')
    grats.add('kittens')
    result = grats.format()
    assert result == "Be grateful for: puppies, kittens"

def test_three_items():
    grats = Gratitudes()
    grats.add('puppies')
    grats.add('kittens')
    grats.add('candy')
    result = grats.format()
    assert result == "Be grateful for: puppies, kittens, candy"