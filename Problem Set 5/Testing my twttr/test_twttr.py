from twttr import shorten

def test_default():
    assert shorten("") == ""

def test_number():
    assert shorten("012") == "012"

def test_word():
    assert shorten("word") == "wrd"

def test_str():
    assert shorten("Good morning!") == "Gd mrnng!"

def test_str_cap():
    assert shorten("gOOd mOrnInG") == "gd mrnnG"
