from numb3rs import validate


def test_first_byte():
    assert validate("255.256.257.258") == False


def test_positive():
    assert validate("127.0.0.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.4") == True


def test_string():
    assert validate("cat") == False
    assert validate("1.2.3.cat") == False
    assert validate("1.dog.duck.cat") == False


def test_incorrect_byte():
    assert validate("1000.1.2.3") == False
    assert validate("1.1000.2.3") == False
    assert validate("1.2.1000.3") == False
    assert validate("1.2.3.1000") == False
    assert validate("1.1000.1001.1002") == False
    assert validate("-1.0.0.1") == False
    assert validate("1") == False
