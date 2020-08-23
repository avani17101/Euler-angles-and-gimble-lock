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
    depth = np.asarray(depth)
    #Now reading the image as a NumPyarray.
    depthModda = o3d.geometry.Image((depth * 0.001).astype(np.float32))
    #Scaling the values of depth given and converting to an Image file.
    o3d.io.write_image("./depthModda.png", depthModda)
    #Writing the new image file.
    display(colour)
    display(depth)
    display(depthModda)
    rgbdImage = o3d.geometry.RGBDImage.create_from_color_and_depth(colour, depthModda)
    #Creating the rgbd image.
    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbdImage, o3d.camera.PinholeCameraIntrinsic(o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))
    #Giving camera parameters.
    pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    #flipping the axis as open3D has +ve y in the direction of gravity
    o3d.visualization.draw_geometries([pcd])
