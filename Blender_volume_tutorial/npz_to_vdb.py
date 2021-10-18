import numpy as np
import pyopenvdb as vdb

def Scale_data(data):
	return data/(data.max()-data.min())

data = np.load('./IllustrisTNG_128.npz')
output_name = 'CCA_tutorial_illustrisTNG.vdb'


N_res = 128
Mgas = Scale_data(data['Mgas'])
T = Scale_data(data['T'])
Z = Scale_data(data['Z'])



dataCube = []

dataCube.append(vdb.FloatGrid())
dataCube[-1].copyFromArray(Mgas)
dataCube[-1].name = 'Mgas'
dataCube[-1].transform = vdb.createLinearTransform(voxelSize=1/(N_res))

dataCube.append(vdb.FloatGrid())
dataCube[-1].copyFromArray(T)
dataCube[-1].name = 'T'
dataCube[-1].transform = vdb.createLinearTransform(voxelSize=1/(N_res))

dataCube.append(vdb.FloatGrid())
dataCube[-1].copyFromArray(Z)
dataCube[-1].name = 'Z'
dataCube[-1].transform = vdb.createLinearTransform(voxelSize=1/(N_res))


vdb.write(output_name, grids=dataCube)
