import pytest
import pathlib
import importlib

SOLUTION = pathlib.Path("solution.py")

def _test_file(p=SOLUTION):
    if not p.exists():
        raise AssertionError(f"Solution file '{p}' is missing.")

def _test_variable(name, reference, mod=SOLUTION):
    try:
        module = importlib.import_module(mod.stem)
    except ImportError:
        raise AssertionError(f"Solution file '{mod}' could not be imported")
    try:
        value = getattr(module, name)
    except AttributeError:
        raise AssertionError(f"Solution file '{mod}' does not contain variable '{name}'.")

    assert value == pytest.approx(reference), f"{name}={value} is not correct"
