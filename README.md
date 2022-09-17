# `hypothesis-blns`

## Why?

Inspired by the many talks and workshops at
[PyCon UK 2022](https://2022.pyconuk.org/) covering
[*Hypothesis*](https://hypothesis.readthedocs.io/).

## What?

Hypothesis already has a
[`text()`](https://hypothesis.readthedocs.io/en/latest/data.html#hypothesis.strategies.text)
strategy which will generate strings for testing. The
[Big List of Naughty Strings](https://github.com/minimaxir/big-list-of-naughty-strings/)
provides a specific set of notorious strings which can be useful in testing
assumptions around the stability of a functions handling of strings.

## How?

```python

from hypothesis import given, strategies

from hypothesis_blns.strategies import blns


def should_handle_strings_sensibly(input: str) -> str:
    ...


@given(blns())
def test_blns(naughty: str):
   result = should_handle_strings_sensibly(naughty) 
   ...

```

## Really?

Yeah, in hindsight throwing the whole set through a function via
[`@pytest.mark.parametrize`](https://docs.pytest.org/en/6.2.x/parametrize.html)
or similar would make more sense: there aren't that many values.

Oh well…
