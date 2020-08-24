import open3d as o3d
import math
import copy
import numpy as np
from scipy.linalg import logm
from scipy.spatial.transform import Rotation as R
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

#A matrix is a valid rotation matrix is MM' = M'M = I.
#det(M) = 1

M_given =  np.array([[0.26200263, -0.19674724, 0.944799],
                     [0.21984631, 0.96542533, 0.14007684],
                     [-0.93969262, 0.17101007, 0.29619813]])

N_given = np.array([[0,-0.173648178,0.984807753],
                    [0, 0.984807753, 0.173648178],
                    [-1, 0, 0]])

def validRotation(mat):
    matT = np.transpose(mat)
    dim = mat.shape
    #print(dim)
    checker = np.matmul(mat, matT)
    for i in range(dim[0]):
        for j in range(dim[1]):
            #print(i , end = " ")
            #print(j , end = " ")
            #print(checker[i][j])
            if(i != j):
                if(abs(checker[i][j]) > 0.0001):
                    return False
            else:
                if abs(1 - checker[i][j]) > 0.0001:
                    return False
    return True

#print(validRotation(M_given))

#Turns out the XYZ, ZYX Euler angles will be the same when calculated from the rotation matrix.

if validRotation(M_given):
    sy = math.sqrt(M_given[0][0] * M_given[0][0] +  M_given[1][0] * M_given[1][0])
    alpha = math.atan2(M_given[2][1], M_given[2][2])
    beta = math.atan2(M_given[2][0], sy)
    gamma = math.atan2(M_given[1][0], M_given[0][0])
    print(alpha)
    print(beta)
    print(gamma)

    r = R.from_euler('zyx', [[alpha, beta, gamma]], degrees = True)
    #print(type(r))
    #print(r.as_quat().shape)
    #Prints r as quaternion
    print(r.as_matrix())

if validRotation(N_given):
    sy = math.sqrt(N_given[0][0] * N_given[0][0] +  N_given[1][0] * N_given[1][0])
    alpha = math.atan2(N_given[2][1], N_given[2][2])
    beta = math.atan2(N_given[2][0], sy)
    gamma = math.atan2(N_given[1][0], N_given[0][0])
    print(alpha)
    print(beta)
    print(gamma)

    r = R.from_euler('zyx', [[alpha, beta, gamma]], degrees = True)
    #print(type(r))
    #print(r.as_quat().shape)
    #Prints r as quaternion
    print(r.as_matrix())
