Introduction to Blender
===
###### tags: `Visualization`

Prerequisite:

1. Download [blender](https://www.blender.org/download/). The version of blender we use in this tuotrial is 2.93.5
2. Having a mouse with scroll wheel helps navigating in the blender viewport a lot.
3. Checkout the github repo for [this tutorial](https://github.com/kazewong/Blender_volume_tutorial). 
4. Install pyopenvdb, which requires python version >= 3.7. Depending on your python version, you can do either pip install pyopenvdb or pyopenvdb-3.8. 

Notes:
1. I capture the screen on a 4K monitor, so the images could look a bit small here. If you have trouble reading it, you can right click the images to open it in a new tab, then zoom into region you want to check.

# Setting up the workspace

1. Set the background of the world to black. You should not see any change in the background color yet. 
![](https://i.imgur.com/zX2mEi2.png)
2. Change the render engine from Eevee to Cycles. If you have a gpu, you can also change the device to gpu. ![](https://i.imgur.com/ZHPWwDu.png)
3. Go to `Edit->Preferences->Input`, and enable `emulate Numpad`. This will drastically increase your ability to navigate in the viewport without a number pad.
4. Go to `Edit->Preferences->Add-ons`, search for `Node Wrangler` and enable it.




# Importing volume data into blender

1. Download the datafile 'IllustrisTNG_128.npz'
2. In shell, run `python script npz_to_vdb.py`, you should have the file`CCA_tutorial_illustrisTNG.vdb`
3. Open blender, start with a 
4. Delete the default cube by <kbd>left click</kbd> the cube to select it, then press <kbd>x</kbd> to delete it.
5. Press <kbd>SHIFT</kbd>+<kbd>a</kbd> to open the drop down menu for adding object, choose volume->ImportOpenVDB. Choose the vdb file you just created with the python script. ![](https://i.imgur.com/7Hq71qY.png) 
6. You should have something like this ![](https://i.imgur.com/j9Ku16s.jpg)
7. Change `clipping` to 0. Then play around with `density` to see the structure of `Mgas`. Start with setting `density` to 1000.
8. Check the temperature field `T` and metallicity field `Z` as well.
9. Your view should look some like the following picture at this point. ![](https://i.imgur.com/3z6mrB2.jpg)

# Basic navigation
1. Center the cube at the origin by setting `transform->location X,Y,Z` in `object properties` to -0.5. ![](https://i.imgur.com/taDr9yd.png)
2. Scroll up the scroll wheel to zoom into the object.
3. Press down the scroll wheel then drag to rotate around the object.
4. Try `walk navigation` in the `View->Navigation` menu, then use <kbd>W</kbd> <kbd>A</kbd> <kbd>S</kbd> <kbd>D</kbd> together with your mouse to navigate around the cube.
5. Press <kbd>`</kbd> to call the view menu, pick a few to see the cube in different angle.
6. Pick an angle you like, then <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>0</kbd> to set the camera to the current view.


# Basic shading

1. Right click the vertical boundary of the 3D viewport and the properties tab, choose `Vertical split`, the drag to the left to create a new split in the workspace. ![](https://i.imgur.com/pG5vDeA.png) ![](https://i.imgur.com/eCVLNqq.png)
2. Go to the top left of the right split. Click the dropdown menu and pick `Shade Editor`. ![](https://i.imgur.com/3xJOJwn.png)
3. Go to the top and press `+ new`, that should add some material nodes in the split. ![](https://i.imgur.com/yeiZH26.png) 
You should see the following nodes. ![](https://i.imgur.com/EKBBmvm.png)
4. Go to the top right of the left split, select the right most icon as shown in the figure below. This will change the viewport from 3D viewport to the render viewport. ![](https://i.imgur.com/T2zrtQ4.png)


## Emission strength

The first thing we want to work on is to make our volume luminous.

1. Set the 'density' field to 0.
2. Delete the input for `Density Attribute` and `Temperature Attribute`.
3. Press <kbd>Shift</kbd>+<kbd>a</kbd> to call the add node menu. Search for the `Attribute` node and add it. Put `Mgas` in the `Name` field.
4. Drag the `Fac` node and drop it in `Emission Strength` of the `Principled Volume` Node. You should see an empty black background in the render viewport now.
5. Call the add node menu with <kbd>Shift</kbd>+<kbd>a</kbd> again to add a `Math` node (`Converter->Math`). Click the drop down menu and choose `Multiply` from the menu. Connect the output from the `Attribute` node to one of the `Value` input of the `Math` node, then connect the output of `Math` node to the `Emission Strength` of the `Principled Volume` node. Change the other `Value` input of the `Math` node to around 1000. You should then see the large scale structure of the volume data.
6. Right click the `Math` node then press <kbd>Shift</kbd>+<kbd>d</kbd> to duplicate the node. Drag and drop it to the connection between the `Attribute` node and the `Math` node. Change this node from `Multiply` to `Power`. Adjust the exponent to increase/decrease the contrast of the field.

This is how the node tree and the volume should look like at this stage.
![](https://i.imgur.com/zYbVv7l.png)
![](https://i.imgur.com/T95npdv.png)

## Color

The next thing we want is to add color to our volume.

1. Add another `Attribute` node to the node tree, set the name to `T`, which is the temperature of the field.
2. Add a `Converter->ColorRamp` node to the node tree, connect the output of the `Attribute` to the `Fac` input of the `ColorRamp` node, and connect the `Color` output to the `Emission Color` to the `Principled Volume` node.
3. Duplicate the `Power+Multiply` nodes from the Emission stength part, then apply to the output of the `Attribute` node with `T` as its name. Adjust that until you have a satisfying result in the color.

This is how the node tree and the volume should look like at this stage.
![](https://i.imgur.com/x7AjWHI.png)
![](https://i.imgur.com/QuoOIog.png)



## Absorption
1. Add another `Attribute` node to the node tree, set the name to `Z`, which is the metalicity of the field.
2. Add a `Shader->Volume absorption` node to the node tree, connect the output of the `Attribute` to the `Density` input of the `Volume absorption` node.
3. Add a `Shader->Add Shader` node to the node tree.
4. Combine the `Volume` output of both the `Principled Volume` nodeand the `Volume absorption` node into the input of `Add Shader`, then connect the output of `Add Shader` to the `Volume` attribute of the `Material Output`.
5. You can adjust the stength and contrast of the absorption using the `Power+Multiply` node again.

The absorption is a more subtle effect that is more interesting when you fly through the volume.

This is how the node tree and the volume should look like at this stage.
![](https://i.imgur.com/NV8x4fR.png)
![](https://i.imgur.com/9b4DDZ8.png)

# Camera movement

The next thing we will work on is to move a camera around the volume to create a rotating view of the volume.

1. Go back to the normal 3D viewport ![](https://i.imgur.com/temDOEM.png)
2. Use <kbd>Shift</kbd>+<kbd>a</kbd> to add an `Empty->Plain axes` object to the scene.
![](https://i.imgur.com/cUadjSw.png)
2. Add a `Curve->Circle` to the scene
![](https://i.imgur.com/MCbTTXt.png)
3. Left click the circle you just created. Press <kbd>s</kbd> and drag to scale the circle to a larger size. Then left click to confirm the change. After that, press <kbd>g</kbd> then <kbd>z</kbd> to grab the circle and move it along the z-axis.
![](https://i.imgur.com/4Y7DJt4.png)
4. Press <kbd>Tab</kbd> to enter the edit mode. Select one of the node point on the circle, then press <kbd>Shift</kbd> + <kbd>s</kbd> and selection `Cursor to Selected` to move the 3D cursor to the node point. Hit <kbd>Tab</kbd> again, when you are done.
![](https://i.imgur.com/dILmp8Z.png)
![](https://i.imgur.com/shteSBD.png)
5. First select the Camera, then hold <kbd>Shift</kbd> and select the circle. Press <kbd>Ctrl</kbd> + <kbd>p</kbd> to pull the parent menu. Choose `Follow Path` from the menu.
![](https://i.imgur.com/IqBWQai.png)
6. Left click somewhere else on the screen to deselect the objects. Then choose the camera again, go to the properties on the right and the icon with a crankshaft. Click `Add Object Constraint` then choose `Track To`. Then pick the `Target` to be the `Empty`.
![](https://i.imgur.com/wyZqrgw.png)
![](https://i.imgur.com/YoaueLk.png)
7. Finally, select the circle we created, go to the properties tab with a curve on it, go to `Path Animation` field, and set `Frames` to 360.
![](https://i.imgur.com/V8O1idS.png)
8. Now go to the time sliders at the bottome, drag the time sliders around to see the camera moves. You can also go to the camera view with <kbd>`</kbd>.
![](https://i.imgur.com/FgAKip6.png)

We will let the a camera goes in circle 

# Rendering

1. Go to the panel on the right, click on the icon that look like a camera. Choose render and viewport to be 1. This drastically reduce the rendering time. Note that this is usually a terrible choice since there will be a lot of aliasing in the final render. But for our case this is actually fine. ![](https://i.imgur.com/Sh1yq9L.png)

2. On the same panel, click the third icon that look like a printer printing an image. Choose the `Frame End` to be 360, and change the output to a directory where you want to output the rendered images and video. You can also set the fps to 60 to have a smoother video. ![](https://i.imgur.com/4521UEJ.png)

3. Go to the top tab and press `Render->Render Animation`. This will generate a series of PNG in the folder you chose to be the output folder.![](https://i.imgur.com/OtgVvVF.png)

4. After finish rendering the series of PNG, switch one of the split to the `Video Sequencer` view. ![](https://i.imgur.com/pseSnU9.png)
5. Click `Add` on the top of the split. Choose `Image Sequence` and choose the series of png you just rendered.
6. Now go to the properties tab on the right and choose the render tab again. Change file format to `FFmpeg video`. Open the `Encoding` menu, choose the container to be `MPEG-4`, the `Output Quality` to be `Perceptually Lossless`, and `Encoding Speed` to be `Slowest`.![](https://i.imgur.com/8niauHn.png)
7. `Render->Render Animation` again and you should have the video!

