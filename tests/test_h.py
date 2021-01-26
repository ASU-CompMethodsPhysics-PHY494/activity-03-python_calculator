import pytest

from .tst import _test_variable

def test_h(name='h', reference=1.99999945):
    return _test_variable(name, reference)

