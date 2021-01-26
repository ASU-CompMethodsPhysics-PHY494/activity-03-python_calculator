import pytest

from .tst import _test_variable

def test_b(name='b', reference=-99):
    return _test_variable(name, reference)

