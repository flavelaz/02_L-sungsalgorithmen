import pytest

def erhoben_um_eins(x):
    return x+1

def test_erhoben_um_eins_correct():
    assert erhoben_um_eins(3)==4,"3+1 sollte 4 sein"

def test_erhoben_um_eins_incorrect():
    assert erhoben_um_eins(3)==6,"3+1 sollte 4 sein"