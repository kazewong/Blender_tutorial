import numpy as np
import h5py
import pyopenvdb as vdb
import os
### PUT THE athena_read.py in your path
import athena_read

path = '/mnt/home/wwong/ceph/Simulations/Athena/blast3d'

for index in range(11):
	data_prim = athena_read.athdf('/mnt/home/wwong/ceph/Simulations/Athena/blast3d/Blast.out1.'+str(index).zfill(5)+'.athdf')
	x = data_prim['x1f'] # x pos of cell faces
	y = data_prim['x2f'] # y pos of cell faces
	z = data_prim['x3f'] # z pos of cell faces
	xv = data_prim['x1v'] # x pos of cell centers
	yv = data_prim['x2v'] # y pos of cell centers
	zv = data_prim['x3v'] # z pos of cell centers
	rho = data_prim['rho'] # density at cell center
	press = data_prim['press'] # pressure at cell center
	vel1 = data_prim['vel1'] # x velocity at cell center
	vel2 = data_prim['vel2'] # y velocity at cell center
	vel3 = data_prim['vel3'] # z velocity at cell center

# 	output_dir = '/mnt/home/wwong/ceph/Visualization/Turbulance/vdb/'
# 	N_res = 512
# 	output_tag = 'mixing_layer_chi100_Mach05_'+str(N_res)+'.'+str(index).zfill(5)+'.vdb'
	
	
# 	dataCube = []
# 	density = rho#normalize_data(rho)
# 	velocity = np.array([vel1,vel2,vel3])
# 	velocity = velocity#normalize_data(velocity)
# #	velocity = velocity - np.median(velocity)
	
# 	dataCube = []
	
# 	scale_factor = 1
	
# 	dataCube.append(vdb.FloatGrid())
# 	dataCube[-1].copyFromArray(density)
# 	dataCube[-1].name = 'density'
# 	dataCube[-1].transform = vdb.createLinearTransform(voxelSize=scale_factor/(N_res))
# 	maskCube = vdb.FloatGrid()
	
# 	for i in range(3):
# 	    dataCube.append(vdb.FloatGrid())
# 	    dataCube[-1].copyFromArray(velocity[i])
# 	    dataCube[-1].name = 'velocity'+str(i)
# 	    dataCube[-1].transform = vdb.createLinearTransform(voxelSize=scale_factor/(N_res))
	
	
# 	output_name = output_dir+output_tag
# 	vdb.write(output_name, grids=dataCube)
