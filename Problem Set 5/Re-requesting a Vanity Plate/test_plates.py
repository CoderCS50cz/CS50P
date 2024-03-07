from plates import is_valid


def test_default():
    assert is_valid("") == False

def test_one_arg():
    assert is_valid("a") == False

def test_too_many_arg():
    assert is_valid("abc1234") == False

def test_digit_first_arg():
    assert is_valid("0abcde") == False

def test_zero_fird_arg():
    assert is_valid("ab012") == False

def test_digit_in_middle():
    assert is_valid("ab12cd") == False

def test_no_punctuation():
    assert is_valid("a.b123") == False

def test_under_conditions():
    assert is_valid("ab1234") == True

def test_no_alphabet_begin():
    assert is_valid("12") == False

def test_no_alphanum():
    assert is_valid("cs.") == False
