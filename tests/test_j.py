import pytest

from .tst import _test_variable

def test_j(name='j', reference=1.4142135623730951):
    return _test_variable(name, reference)

