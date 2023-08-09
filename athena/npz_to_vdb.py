import numpy as np
import pyopenvdb as vdb

data = np.load('blast3d.npz')
N_res = 64


output_name = 'blast3d'

field_name = ['rho','press', 'vel1', 'vel2', 'vel3']

for i in range(len(data['rho'])):
	dataCube = []

	for name in field_name:
		dataCube.append(vdb.FloatGrid())
		dataCube[-1].copyFromArray(data[name][i])
		dataCube[-1].name = name
		dataCube[-1].transform = vdb.createLinearTransform(voxelSize=1/(N_res))
		vdb.write(output_name+'_'+str(i)+'.vdb', grids=dataCube)
