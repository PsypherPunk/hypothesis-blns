import json
import pathlib

from hypothesis import strategies

from hypothesis_blns import _data

with open(pathlib.Path(_data.__file__).parent / "blns.json") as i:
    _BLNS = json.load(i)


def blns() -> strategies.SearchStrategy[str]:
    """
    Creates a strategy yielding values from the Big List of Naughty Strings™.
    """
    return strategies.sampled_from(_BLNS)
