from hypothesis import given, strategies

from hypothesis_blns.strategies import blns


@given(blns())
def test_blns(input: str):
    assert isinstance(input, str)
