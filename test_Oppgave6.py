import pytest
from calculator import add

# Oppgave 1
@pytest.mark.parametrize("x, y, z", [(1,1,2), (2,2,4), (3,3,6)])
def test_add_exercise_1(x,y,z):
    assert add(x, y) == z


# Oppgave 2
@pytest.mark.parametrize("x, y, z", [(0.1,0.1,0.2), (0.2,0.2,0.4), (0.3,0.3,0.6)])
def test_add_exercise_2(x,y,z): 
    assert abs(add(x, y)) - z < 1e-12


# Oppgave 3
@pytest.mark.parametrize("x,y,z", [("Hello ","world","Hello world"), ("boom ","boom","boom boom")])
def test_add_exercise_3(x,y,z):
    assert add(x, y) == z


# Oppgave 4
import math
import numpy as np
from Oppgave4 import factorial
from Oppgave4 import sin
from Oppgave4 import divide
from Oppgave4 import exponent
from Oppgave4 import transpose

@pytest.mark.parametrize("x", [(5), (3), (7)])
def test_factorial_exercise_4(x):
    assert factorial(x) == math.factorial(x)

@pytest.mark.parametrize("x, N", [(math.pi, 25), (math.pi/2, 40), (math.pi/3, 35)])
def test_sin_exercise_4(x, N):
    assert sin(x, N) - np.sin(x) < 1e-8

@pytest.mark.parametrize("x, y", [(7, 2), (88, 4), (1.3,3)])
def test_divide_exercise_4(x,y):
    assert divide(x,y) == x / y

@pytest.mark.parametrize("x, y, z", [(5,2,25), (3,3,27), (7,2,49)])
def test_exponent_exercise_4(x,y,z):
    assert exponent(x, y) == z

@pytest.mark.parametrize("x, y", [([[1,2],[3,4]],[[1,3],[2,4]]) , 
                    ([[1,2,3],[4,5,6],[7,8,9]],[[1,4,7],[2,5,8],[3,6,9]])])
def test_transpose_exercise_4(x,y):
    assert transpose(x) == y


# Oppgave 5
from calculator import add
from Oppgave4 import divide
import pytest

@pytest.mark.parametrize("x, y", [("Hello", 2), ("World", 4), (4,"four")])
def test_TypeError_exercise_5(x,y):
    with pytest.raises(TypeError):
        add(x, y)

@pytest.mark.parametrize("x, y", [(2, 0), (3, 0), (1,0)])
def test_ZeroDivisionError_exercise_5(x,y):
    with pytest.raises(ZeroDivisionError):
        divide(x,y)






