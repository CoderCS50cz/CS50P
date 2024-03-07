from seasons import convert
import pytest


def test_incorrect_format():
    with pytest.raises(SystemExit):
        convert("January 1, 2023")

def test_type_mistake():
    with pytest.raises(SystemExit):
        convert("1999.01.01")

def test_correct_date():
    assert convert("2022-12-17") == "Five hundred twenty-five thousand, six hundred minutes"
