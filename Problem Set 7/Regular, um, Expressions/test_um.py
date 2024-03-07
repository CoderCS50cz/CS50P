from um import count


def test_right_word():
    assert count("um") == 1

def test_digit():
    assert count("0") == 0

def test_text_two_words():
    assert count("Hello, um, how are, um ...") == 2

def test_look_a_like():
    assert count("Look's yummy!") == 0

def test_case_insensitive():
    assert count("Um, um, uM, UM") == 4
