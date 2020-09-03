from calculator import add

def test_add_exercise_1():
    assert add(1, 2) == 3

def test_add_exercise_2():
    assert abs(add(0.1, 0.2)) - 0.3 < 1e-12

def test_add_exercise_3():
    assert add("Hello ", "world") == "Hello world"
