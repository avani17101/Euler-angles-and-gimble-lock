# Transformations

Libraries used: Open3D

## Converting RGBD image into Point Cloud
Convert RGBD from Sun images to point cloud.
**Dataset** [SUN RGB-D dataset](https://rgbd.cs.princeton.edu/), S.Song, CVPR 2015
**Steps**
* Read the two images color.jpg and depth.png given in current folder using Open3D.
* Convert it to a point cloud using the default camera parameters
* Create a "world" frame and combine this (just use operator) with the above point cloud and save it as scene.pcd.
* A simple function one_one to visualize scene.pcd.

## Rotations, Euler angles and Gimbal Lock

### Rotating an object
**Steps**
* Generate a cube at some point on the ground and create another frame at the center of this object.
* Combine those as a single point cloud cube.pcd. 
* Read both the point clouds scene.pcd and cube.pcd in a script.
* Given a sequence of ZYX Euler angles, generate the rotation. 
* Function two_one to show the above by animation (cube rotating along each axis one by one)
**Note** Throughout this assignment, the standard ZYX Euler angle convention is used.

### Euler angle & Gimbal lock
###  Rotation matrix as an Operator

