import pytest
from hugs.calc import get_wind_components
import numpy as np
from numpy.testing import assert_almost_equal, assert_array_almost_equal
import pytest

def test_wind_comp_scalar():
    speed = 10.
    wdir = 200.
    u,v = get_wind_components(speed, wdir)
    uu = -speed * np.sin(np.radians(wdir))

    assert_almost_equal(u,uu,3)
    
def test_wind_comp_array():
    speed = np.array([10.,20.,30.])
    wdir  = np.array([1.,2.,3.])
    u, v = get_wind_components(speed, wdir)
    assert np.size(u) == 3
    
def test_warning_direction():
    "Test raising when direction greater than 360"
    with pytest.warns(UserWarning):
        get_wind_components(3., 400.)
