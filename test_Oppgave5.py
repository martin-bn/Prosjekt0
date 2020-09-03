from calculator import add
from Oppgave4 import divide

import pytest

def test_TypeError_exercise_5():
    with pytest.raises(TypeError):
        add("Hello", 1)

def test_ZeroDivisionError_exercise_5():
    with pytest.raises(ZeroDivisionError):
        divide(2,0)
