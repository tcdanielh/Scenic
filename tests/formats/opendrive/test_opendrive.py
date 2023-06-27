
import os
import glob
from pathlib import Path

import matplotlib.pyplot as plt
import pytest

from scenic.formats.opendrive import OpenDriveWorkspace
from scenic.core.geometry import TriangulationError

mapFolder = Path(__file__).parent.parent.parent.parent / 'assets' / 'maps'
maps = glob.glob(str(mapFolder / '**' / '*' / '.xodr'))

@pytest.mark.slow
@pytest.mark.filterwarnings("ignore::scenic.formats.opendrive.OpenDriveWarning")
@pytest.mark.parametrize("path", maps)
def test_map(path, runLocally, pytestconfig):
    with runLocally():
        try:
            odw = OpenDriveWorkspace(path, n=10)
        except TriangulationError:
            pytest.skip('need better triangulation library to run this test')
        pt = odw.drivable_region.uniformPointInner()
        odw.road_direction[pt]
        if not pytestconfig.getoption('--no-graphics'):
            odw.show(plt)
            plt.show(block=False)
            plt.close()
