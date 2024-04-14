import numpy as np
from read_data import ReadData
from scipy.interpolate import griddata

d = ReadData("disk.out1.00100.athdf") # read data and grid into numpy arrays

r = d['x1v']
theta = d['x2v']
phi = d['x3v']
rho = d['rho']
grid = np.meshgrid(r, theta, phi,indexing='ij')
r, theta, phi = grid

x = (r*np.sin(theta)*np.cos(phi)).flatten()
y = (r*np.sin(theta)*np.sin(phi)).flatten()
z = (r*np.cos(theta)).flatten()
rho = rho.flatten()

N_grid = 128
new_axis = np.linspace(-2, 2, N_grid)
new_grid = np.meshgrid(new_axis, new_axis, new_axis)
new_x, new_y, new_z = new_grid
new_x = new_x.flatten()
new_y = new_y.flatten()
new_z = new_z.flatten()
new_r = np.sqrt(new_x**2 + new_y**2 + new_z**2)

interp_rho = griddata(np.array([x, y, z]).T, rho, np.array([new_x, new_y, new_z]).T)

interp_rho[np.isnan(interp_rho)] = 0

np.savez('./processed_disk', interp_rho=interp_rho.reshape(N_grid, N_grid, N_grid))