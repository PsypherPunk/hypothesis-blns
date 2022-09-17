import pathlib

from setuptools import find_packages, setup

with open(pathlib.Path(__file__).parent / "requirements/base.txt") as i:
    requirements = [r.split("==")[0] for r in i]


setup(
    name="hypothesis-blns",
    version="0.1.0",
    description="Big List of Naughty Strings extension for Hypothesis.",
    author="PsypherPunk",
    author_email="psypherpunk",
    url="https://github.com/PsypherPunk/hypothesis-blns",
    packages=find_packages(
        include=("hypothesis_blns", "hypothesis_blns.*"),
    ),
    install_requires=requirements,
)
