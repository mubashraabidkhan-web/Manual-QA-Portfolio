from string_utils import reverse_string, is_palindrome, count_vowels

def test_reverse_string():
    assert reverse_string("abc") == "cba"

def test_is_palindrome_true():
    assert is_palindrome("madam") is True

def test_is_palindrome_false():
    assert is_palindrome("hello") is False

def test_count_vowels():
    assert count_vowels("Hello") == 2
    