from setuptools import setup, find_packages
from pathlib import Path


setup(
    name="sec_parsers",
    author="John Friedman",
    version="0.530",
    description="A package to parse SEC filings",
    long_description_content_type='text/markdown',
    packages=find_packages(include=['sec_parsers', 'sec_parsers.*']),
    install_requires=[
        'lxml', 
        'requests',
    ],
    entry_points={
        "console_scripts": [
            "extract-compensation=sec_parsers.extract_compensation:main",
        ],
    },
)
