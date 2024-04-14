import bpy
import numpy as np
from mathutils import Vector


data = np.load('/home/wwong/Mar_void_point.npz')

scale = max([data['x'].max()-data['x'].min(), data['y'].max()-data['y'].min(), data['z'].max()-data['z'].min(), data['vx'].max()-data['vx'].min(), data['vy'].max()-data['vy'].min(), data['vz'].max()-data['vz'].min()])
down_sample = 10

x = data['x'][::down_sample]/scale
y = data['y'][::down_sample]/scale
z = data['z'][::down_sample]/scale
vx = data['vx'][::down_sample]/scale
vy = data['vy'][::down_sample]/scale
vz = data['vz'][::down_sample]/scale
M = data['M'][::down_sample]

verts = []


for i in range(0,x.shape[0],1):
    verts.append(Vector((x[i], y[i], z[i])))


obj_name = "MyObj"
mesh_data = bpy.data.meshes.new(obj_name + "_data")
obj = bpy.data.objects.new(obj_name, mesh_data)
bpy.context.scene.collection.objects.link(obj)
mesh_data.from_pydata(verts, [], [])

obj.data.attributes.new(name='vx', type='FLOAT', domain='POINT')
obj.data.attributes['vx'].data.foreach_set('value', vx)
obj.data.attributes.new(name='vy', type='FLOAT', domain='POINT')
obj.data.attributes['vy'].data.foreach_set('value', vy)
obj.data.attributes.new(name='vz', type='FLOAT', domain='POINT')
obj.data.attributes['vz'].data.foreach_set('value', vz)
obj.data.attributes.new(name='M', type='FLOAT', domain='POINT')
obj.data.attributes['M'].data.foreach_set('value', M)