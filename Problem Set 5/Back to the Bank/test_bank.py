from bank import value


def test_default():
    assert value("") == 100

def test_zero():
    assert value("0") == 100

def test_hello():
    assert value("hello") == 0

def test_h():
    assert value("hi") == 20

def test_str():
    assert value("Good morning!") == 100

def test_str_cap():
    assert value("Hello") == 0
