import pytest

from .tst import _test_file as test_file_exists
from .tst import _test_variable

def test_a(name='a', reference=1):
    return _test_variable(name, reference)

