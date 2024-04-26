import bpy
import numpy as np
from mathutils import Vector

data = np.load('./Tutorial/quijote/processed_data.npz')

x_g, y_g, z_g = data['x_g'], data['y_g'], data['z_g']
vx_g, vy_g, vz_g = data['vx_g'], data['vy_g'], data['vz_g']
x_v, y_v, z_v = data['x_v'], data['y_v'], data['z_v']
radius_v = data['radius_v']

verts = []

for i in range(0,x_g.shape[0],1):
    verts.append(Vector((x_g[i], y_g[i], z_g[i])))

obj_name = "Halos"
mesh_data = bpy.data.meshes.new(obj_name + "_data")
obj = bpy.data.objects.new(obj_name, mesh_data)
bpy.context.scene.collection.objects.link(obj)
mesh_data.from_pydata(verts, [], [])
obj.data.attributes.new(name='vx', type='FLOAT', domain='POINT')
obj.data.attributes['vx'].data.foreach_set('value', vx_g)
obj.data.attributes.new(name='vy', type='FLOAT', domain='POINT')
obj.data.attributes['vy'].data.foreach_set('value', vy_g)
obj.data.attributes.new(name='vz', type='FLOAT', domain='POINT')
obj.data.attributes['vz'].data.foreach_set('value', vz_g)

verts = []

for i in range(0,x_v.shape[0],1):
    verts.append(Vector((x_v[i], y_v[i], z_v[i])))

obj_name = "Voids"
mesh_data = bpy.data.meshes.new(obj_name + "_data")
obj = bpy.data.objects.new(obj_name, mesh_data)
bpy.context.scene.collection.objects.link(obj)
mesh_data.from_pydata(verts, [], [])

obj.data.attributes.new(name='radius_v', type='FLOAT', domain='POINT')
obj.data.attributes['radius_v'].data.foreach_set('value', radius_v)

