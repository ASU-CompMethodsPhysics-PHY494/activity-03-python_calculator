import pytest

from .tst import _test_variable

def test_e(name='e', reference=5.263157894736843):
    return _test_variable(name, reference)

