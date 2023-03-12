import pytest

from server.main import ponder


@pytest.mark.parametrize(
    "string_value,result",
    [
        ("aabghyu", 1000),
        ("aAbghyu", 1000),
        ("wAaAbghyu", 1000),
        ("a4 p5", 7),
        ("a4 p5 4t", 5.25),
        ("a4", 3.5),
    ],
)
def test_double_a(string_value, result):
    assert ponder(string_value) == result
