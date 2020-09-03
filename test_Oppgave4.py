
import math
import numpy as np

from Oppgave4 import factorial
from Oppgave4 import sin
from Oppgave4 import divide
from Oppgave4 import exponent
from Oppgave4 import transpose

def test_factorial_exercise_4():
    assert factorial(5) == math.factorial(5)

def test_sin_exercise_4():
    assert sin(math.pi / 2, 25) - np.sin(math.pi / 2) < 1e-8

def test_divide_exercise_4():
    assert divide(0.4,2) == 0.4 / 2

def test_exponent_exercise_4():
    assert exponent(3, 3) == 27

def test_transpose_exercise_4():
    matrix = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15]]
    assert transpose(matrix) == [[1, 4, 7, 10, 13], [2, 5, 8, 11, 14], [3, 6, 9, 12, 15]]
