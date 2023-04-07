import pytest
from series.series import fibonacci, lucas, sum_series


def test_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_fibonacci_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


def test_fibonacci_seven():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected


def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected


def test_lucas_three():
    actual = lucas(3)
    expected = 4
    assert actual == expected


def test_lucas_7():
    actual = lucas(7)
    expected = 29
    assert actual == expected


def test_sum_series_zero():
    actual = sum_series(0)
    expected = 0
    assert actual == expected


def test_sum_series_one():
    actual = sum_series(1)
    expected = 1
    assert actual == expected


def test_sum_series_two():
    actual = sum_series(2)
    expected = 1
    assert actual == expected


def test_sum_series_one_with_first():
    actual = sum_series(0, 2)
    expected = 2
    assert actual == expected


def test_sum_series_one_with_first_eq_two_and_n_1():
    actual = sum_series(1, 2)
    expected = 1
    assert actual == expected


def test_sum_series_one_with_first_eq_two_and_n_4():
    actual = sum_series(4, 2)
    expected = 7
    assert actual == expected


def test_sum_series_one_with_first_eq_two_and_n_2():
    actual = sum_series(2, 2)
    expected = 3
    assert actual == expected


def test_sum_series_one_with_sec_eq_two_and_n_1():
    actual = sum_series(1, 0, 2)
    expected = 2
    assert actual == expected


def test_sum_series_one_with_sec_one_and_n_2():
    actual = sum_series(2, 0, 1)
    expected = 1
    assert actual == expected