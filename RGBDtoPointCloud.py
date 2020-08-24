import open3d as o3d
import copy
import numpy as np
from scipy.linalg import logm
from scipy.spatial.transform import Rotation as R
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

def display(image):
    plt.imshow(image)
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    colour = o3d.io.read_image("./color.jpg")
    depth = o3d.io.read_image("./depth.png")
    #Reading the images as an image (as opposed to an array).
    #display(colour)
    #display(depth)
    #Creating the rgbd image.
    rgbdImage = o3d.geometry.RGBDImage.create_from_sun_format(colour, depth)
    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbdImage, o3d.camera.PinholeCameraIntrinsic(o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))
    #Giving camera parameters.
    pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    #flipping the axis as open3D has +ve y in the direction of gravity
    o3d.visualization.draw_geometries([pcd])
