import numpy as np

import pygimli as pg
import pygimli.meshtools as mt
from pygimli.physics import ert
import pygimli.meshtools as mt
from pygimli.physics import traveltime
from pygimli.viewer.pv import drawSensors
filename = pg.getExampleFile("ert/modeltank.shm")
shm = pg.DataContainerERT(filename)

for s in shm.sensors():
    plc.createNode(s, marker=-99)