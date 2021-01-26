import pytest

from .tst import _test_variable

def test_c(name='c', reference=121932631979881115785550983112635269):
    return _test_variable(name, reference)

