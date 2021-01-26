import pytest

from .tst import _test_variable

def test_i(name='i', reference=1.5053597082e-10):
    return _test_variable(name, reference)

