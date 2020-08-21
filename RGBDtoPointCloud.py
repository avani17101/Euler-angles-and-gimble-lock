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
    display(colour)
    display(depth)
    rgbdImage = o3d.geometry.RGBDImage.create_from_color_and_depth(colour, depth)

    #print(colour.shape)
    #print(depth.shape)
    #display(rgbdImage)
    print(rgbdImage)
    #pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbdImage, o3d.camera.PinholeCameraIntrinsic(o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))
    #print(pcd)
    #o3d.visualization.draw_geometries([pcd],)
