from calc import calculate
from calc import valid

def test_calculate():
    assert calculate("0+11") == 11
    assert calculate("11+1-3") == 9
    assert calculate("11*2") == 22
    assert calculate("12435+34569-12345*10+50") == eval("12435+34569-12345*10+50")
    assert valid("1+1") == True
    assert valid("11+11*888") == True
    assert valid("*1+1") == False
    assert valid("+++") == False
    assert valid("1") == False
    assert valid("1+") == False
    assert valid("haha") == False