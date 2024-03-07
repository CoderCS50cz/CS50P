import pytest

from fuel import convert, gauge

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_zero_in_convert():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("dog/cat")

def test_numenator_more_denominator():
    with pytest.raises(ValueError):
        convert("4/1")

def test_fraction():
    assert convert("1/4") == 25

def test_percentage():
    assert gauge(1) == "E"

def test_labeling_99():
    assert gauge(99) == "F"

def test_printing_percent():
    assert gauge(50) == "50%"
