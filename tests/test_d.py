import pytest

from .tst import _test_variable

def test_d(name='d', reference=3/2):
    return _test_variable(name, reference)

