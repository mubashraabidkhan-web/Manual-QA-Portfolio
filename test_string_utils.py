from string_utils import reverse_string, is_palindrome, count_vowels

from string_utils import reverse_string, is_palindrome, count_vowels

def test_reverse_string():
    assert reverse_string("abc") == "cba"

def test_is_palindrome_true():
    assert is_palindrome("madam") is True

def test_is_palindrome_false():
    assert is_palindrome("hello") is False

def test_count_vowels():
    assert count_vowels("Hello") == 2

def test_is_palindrome_capital_letters():
    assert is_palindrome("Madam") is True

def test_is_palindrome_empty_string():
    assert is_palindrome("") is True

def test_is_palindrome_with_space():
    assert is_palindrome("race car") is True

def test_racing_car_is_not_palindrome():
    assert is_palindrome("racing car") is False