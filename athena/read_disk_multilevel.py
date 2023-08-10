import numpy as np
import sys
sys.path.append('/mnt/sw/nix/store/6plcgbnkn9w8nf1y0dzmjs1jbjbzi4ma-openvdb-10.0.0/lib64/python3.9/site-packages') # Put your path to openvdb here
### PUT THE athena_read.py in your path
import athena_read
import pyopenvdb as vdb

path = '/mnt/ceph/users/chwhite/athena_data/disk_cartesian.athdf'
output_name = '/mnt/home/wwong/ceph/Visualization/Turbulance/Accretion_disk/disk_cartesian'
N_res = 176
block_size = 22
N_level = 6

field = ['rho', 'press', 'vel1', 'vel2', 'vel3']
data = {}


data_prim = athena_read.athdf(path, raw=True)
logical_location = data_prim['LogicalLocations']
levels = data_prim['Levels']
level_data = []

for name in field:
    field_data = data_prim[name]
    offset = 0
    for level in range(N_level):
        local_data = np.zeros((N_res,N_res,N_res))
        for i in range(field_data.shape[0]):
            if levels[i] == level:
                local_data[(logical_location[i,0]-offset)*block_size:(logical_location[i,0]+1-offset)*block_size,(logical_location[i,1]-offset)*block_size:(logical_location[i,1]+1-offset)*block_size,(logical_location[i,2]-offset)*block_size:(logical_location[i,2]+1-offset)*block_size] = field_data[i].T
        level_data.append(local_data)
        offset = offset*2 + 4
    data[name] = level_data
    
all_scale = 50

for level in range(N_level):
    dataCube = []
    for name in field:
        dataCube.append(vdb.FloatGrid())
        dataCube[-1].copyFromArray(data[name][level])
        dataCube[-1].name = name
        scale = all_scale/(N_res*2**level)
        translate = (all_scale/2)/2**level
        dataCube[-1].transform = vdb.createLinearTransform([[scale, 0, 0, 0],[0, scale, 0, 0],[0, 0, scale, 0], [-translate, -translate, -translate,1]])
    vdb.write(output_name+'_level'+str(level)+'.vdb', grids=dataCube)
