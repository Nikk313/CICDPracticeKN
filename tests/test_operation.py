# Importing the function from src folder
from src.math_operations import add,sub

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    assert add(5,3)==2

def test_sub():
    assert sub(4,2)==2
    assert sub(8,5)==3
    assert sub(6,5)==1
    assert sub(-2,7)==-9