import pytest

from .tst import _test_variable

def test_g(name='g', reference=-81):
    return _test_variable(name, reference)

