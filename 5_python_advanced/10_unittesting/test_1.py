import pytest

def add(a,b):
    return a+b

def test_add():
    assert add(5,5)==10
    assert add(2,5)==7
    assert add(-1,-1)==-2
    assert add(0,0)==0
    assert add(-1,1)==0