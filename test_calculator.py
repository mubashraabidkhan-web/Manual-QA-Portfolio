from calculator import add, is_even

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_is_even_true():
    assert is_even(4) is True

def test_is_even_false():
    assert is_even(7) is False
    assert add (2, 3) ==5
   


