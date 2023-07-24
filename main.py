import numpy as np
import pygimli as pg
import pygimli.meshtools as mt
from pygimli.physics import traveltime
from pygimli.viewer.pv import drawSensors

pyvista = pg.optImport("pyvista")

import matplotlib.pyplot as plt
from pygimli.physics import ert

depth = 0.35
width = 2
length = 3
world = mt.createWorld(start=[0, 0, 0],end=[50,50,-5],marker=1)
block = mt.createCube(size=[2,3,0.35],pos=[25,25,0],boundaryMarker=2)
geom = world + block
pg.show(geom);

n_sensors = 48
sensors = np.zeros((n_sensors, 3))
sensors[0, 0] = 1
sensors[0, 1] = 0
sensors[1:, 0] = -1
sensors[1:, 1] = np.linspace(-1, 1, n_sensors - 1)
scheme = ert.createData(elecs=sensors,schemeName='slm')
for p in scheme.sensors():
    geom.createNode(p)
    #geom.createNode(p - [0, 0.1,0])
    
mesh = mt.createMesh(geom,quality=34)
rhomap = [[1, 10.],
          [2, 75.]]

pg.show(mesh, data=rhomap)