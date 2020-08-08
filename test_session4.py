import pytest
import random
import string
import session4
import os
import inspect
import re
import math

README_CONTENT_CHECK_FOR = [
    'int',
    'encoded_from_base10',
    'digit_map',
    'ValueError',
    'math',
    'isclose',
    'absolute',
    'relative',
    'tolerance',
    'bin(',
    'hex(',
    'round',
    'truncation',
    'error',
    'equality',
    'zero',
    'away'
]

CHECK_FOR_THINGS_NOT_ALLOWED = [
    'math',
    'isclose',
    'bin(',
    'hex(',
    'round(',
    'int(',
    '10.4',
    '-10.4'
    '1.25',
    '-1.25',
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

# def test_readme_contents():
#     readme = open("README.md", "r")
#     readme_words = readme.read().split()
#     readme.close()
#     assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

# def test_readme_proper_description():
#     READMELOOKSGOOD = True
#     f = open("README.md", "r")
#     content = f.read()
#     f.close()
#     for c in README_CONTENT_CHECK_FOR:
#         if c not in content:
#             READMELOOKSGOOD = False
#             pass
#     assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

# def test_readme_file_for_formatting():
#     f = open("README.md", "r")
#     content = f.read()
#     f.close()
#     assert content.count("#") >= 10


