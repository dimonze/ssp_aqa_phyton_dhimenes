from main_app import *


def test_positive():
    assert generate_fibonacci(3) == [1, 1, 2]


def test_negative():
    assert not generate_fibonacci(3) == [1, 1, 3]
