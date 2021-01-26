import pytest

from .tst import _test_variable

def test_m(name='m', reference=1j):
    return _test_variable(name, reference)

