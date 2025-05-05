import sys
import os
import pytest


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fuel_gauge import fuel


@pytest.mark.parametrize(
    "x_p, y_p, expected_p",
    [(1, 2, 50), (1, 10, 10), (0, 1, 0), (0, 1000, 0), (400, 600, 67)],
)
def test_get_percentage(x_p, y_p, expected_p):
    assert fuel.get_percentage(x_p, y_p) == expected_p


@pytest.mark.parametrize(
    "input_r, expected_r",
    [
        (0, "E"),
        (1, "E"),
        (99, "F"),
        (100, "F"),
        (50, "50%"),
        (2, "2%"),
        (98, "98%"),
        (9, "9%"),
        (67, "67%"),
    ],
)
def test_get_result(input_r, expected_r):
    assert fuel.get_result(input_r) == expected_r
