from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar_extra_cap = Jar(100)
    assert jar_extra_cap.capacity == 100


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(3)
    assert jar.size == 4
    jar.deposit(8)
    assert jar.size == 12

    with pytest.raises(ValueError):
        jar.deposit(13)


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(8)
    assert jar.size == 4
    jar.withdraw(2)
    assert jar.size == 2
    jar.withdraw(1)
    assert jar.size == 1

    with pytest.raises(ValueError):
        jar.withdraw(13)
