import pytest

from .tst import _test_variable

def test_f(name='f', reference=7):
    return _test_variable(name, reference)

