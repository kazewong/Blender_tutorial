Visualization volumetric simulations with Blender and Athena++
===
###### tags: `Visualization`
###### Date: August 9 2023

Prerequisite:

1. Download [blender](https://www.blender.org/download/). The version of blender we use in this tuotrial is 3.6.1
2. Having a mouse with scroll wheel helps navigating in the blender viewport a lot.
3. Checkout the github repo for [this tutorial](https://github.com/kazewong/Blender_volume_tutorial/tree/main/athena). 
4. Knowledge about how to run athena, output hdf5, and read them into numpy array.
5. There is an unofficial outdated python pacakge called pyopenvdb, which you would install if you just do pip. Unfortunately, that package is not maintained and doesn't work with python version newer than 3.8. In general I would recommend building openvdb from source then importing their official python binder instead.


# Preparing simulation with Athena++

As a tutorial, we will only run with low res simulation that is easy to run and process. Scaling up shouldn't be to different from what we do here.
1. Run in the root athena directory `python configure.py --prob blast -b --flux hlld -mpi -hdf5`
2. Compile the code with `make clean; make -j4`
3. Change `tlim` to `5` in `inputs/mhd/athinput.blast`, this should gives 51 frames for our video.'
5. Run the code with `mpiexec -n 8 ./bin/athena -i ./inputs/mhd/athinput.blast -d ./data/blast3d/`


# Building Openvdb

As of the time of writing this tutorial, we use [openvdb version 10.0.1](https://github.com/AcademySoftwareFoundation/openvdb/releases/tag/v10.0.1). Here below is the instruction for building openvdb with python support.

1. Clone the [openvdb repository](https://github.com/AcademySoftwareFoundation/openvdb)
2. In the root folder of openvdb, open CmakeLists.txt, and turn on the option for building the python module.
`option(OPENVDB_BUILD_PYTHON_MODULE "Build the pyopenvdb Python module" OFF)`->`option(OPENVDB_BUILD_PYTHON_MODULE "Build the pyopenvdb Python module" ON)`
3. Open `openvdb/openvdb/python/CMakeLists.txt`, and turn on numpy support
`option(USE_NUMPY "Build the python library with numpy support." OFF)` -> `option(USE_NUMPY "Build the python library with numpy support." ON)`
4. Then follow the instructions in the README to build a version of openvdb for your system.

# Converting Athena++ outputs into vdb files

1. In my blender volume tutorial repo, go to [read_file.py](https://github.com/kazewong/Blender_volume_tutorial/blob/main/athena/read_file.py)
2. Replace the path to python site package containing the vdb binder in your system.
3. Change `path` and `output_name` according to where you put the simulations.
4. Change `N_res` and `N_frames` accordingly, which are suppose to be the resolution of your grid and the number of files you have.
5. Add any field you want on top of the standard file given in the file.
6. Run it and you should see a bunch of .vdb files poping up.

# Importing series of vdb into blender

1. When importing the video, make sure you select all the .vdb files, just like as shown below.
![](https://hackmd.io/_uploads/rykZQPWh3.png)
2. On the right panel, you should see something like this. Change the density to a higher number to see the volume.
![](https://hackmd.io/_uploads/HJBXydZ22.png)
3. The rest of the tutorial can follow the illustrisTNG example.
