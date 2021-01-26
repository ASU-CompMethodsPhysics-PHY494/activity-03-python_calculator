import pytest

from .tst import _test_variable

def test_k(name='k', reference=1j):
    return _test_variable(name, reference)

