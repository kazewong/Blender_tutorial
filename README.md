# Visualization in blender tutorial

Reference material and demo file for visualizing a cosmological simualtion in Blender.

`Introduction to blender.html/.md` are the manual you should follow for going through the tutorial. I suggest you use a browser to open the .html file for best experience.

`IllustrisTNG_128.npz` contains 3 numpy arrays from the IllustrisTNG simulation, each with shape (128,128,128).

`npz_to_vdb.py` is a python script that takes the arrays in the .npz file and map it to the .vdb format which blender can read.

`CCA_tutorial_illustrisTNG.vdb` is the volumetric data we will import into Blender.

`IllustrisTNG_128.blend` is the demo file which you have by the end of the tutorial.
