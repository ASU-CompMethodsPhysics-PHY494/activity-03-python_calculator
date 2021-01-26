import pytest

from .tst import _test_variable

def test_l(name='l', reference=-1+3j):
    return _test_variable(name, reference)

