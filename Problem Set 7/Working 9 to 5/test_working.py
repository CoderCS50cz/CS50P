from working import convert
import pytest


def test_string():
    with pytest.raises(ValueError):
        convert("cat")

def test_min_more59():
    with pytest.raises(ValueError):
        convert("9:60 AM to 3:60 PM")

def test_hours_more12():
    with pytest.raises(ValueError):
        convert("13:00 AM to 13:00 PM")

def test_mistake_in_input():
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")

def test_correct_period():
    assert convert("8:00 AM to 5:00 PM") == "08:00 to 17:00"
