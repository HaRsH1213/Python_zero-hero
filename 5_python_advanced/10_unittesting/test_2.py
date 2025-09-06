import pytest

def multiplier(a,b):
    return a*b

def divider(a,b):
    if b==0:
        raise ValueError("Cannot divide by zero")
    return a/b
def test_multiply():
    assert multiplier(3,4)==12
    assert multiplier(5,4)==20
    assert multiplier(2,0)==0
    assert multiplier(-1,5)==-5

def test_divider():
    assert divider(10,2)==5
    assert divider(9,3)==3
    assert divider(10,2)==5
    with pytest.raises(ValueError):
        divider(5,0)