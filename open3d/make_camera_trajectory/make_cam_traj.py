# Open3D: www.open3d.org
# The MIT License (MIT)
# See license file or visit www.open3d.org for details

# examples/python/geometry/camera_trajectory.py

# refer to http://www.open3d.org/docs/release/python_api/open3d.camera.PinholeCameraTrajectory.html for PinholeCameraTrajectory class

import numpy as np
import open3d as o3d

if __name__ == "__main__":

    print("testing make camera trajectory")

    cam = np.load("flower_sketch.npz")
    c2ws = cam['c2ws']
    h = 600 # cam['h']
    w = 800 # cam['w']
    fx = cam['fx']
    fy = cam['fy']
    n = c2ws.shape[0]

    trajectory = o3d.camera.PinholeCameraTrajectory()
    print(trajectory) # Access intrinsics with intrinsic_matrix.
    print(trajectory.parameters) # an empty list []
    l = [] # i donot know why i can not usr trajectory.parameters directly here
    for i in range(n):
        p = o3d.camera.PinholeCameraParameters()
        p.intrinsic = o3d.camera.PinholeCameraIntrinsic(w, h, fx, fy, w/2, h/2)
        p.extrinsic = np.linalg.inv(c2ws[i]) # W2C
        l.append(p)
    trajectory.parameters = l
    print(len(trajectory.parameters))
    print(trajectory.parameters[0].intrinsic.intrinsic_matrix)

    o3d.io.write_pinhole_camera_trajectory("my_trajectory.json", trajectory)
    
    

    
    # # set camera instrinsic
    # # o3d.camera.PinholeCameraIntrinsic(w, h, fx, fy, w/2, h/2) # (width, height, fx, fy, cx, cy)

    # # check camera instrinsic, class open3d.camera.PinholeCameraIntrinsic
    # # 'get_focal_length', 'get_principal_point', 'get_skew', 'height', 'intrinsic_matrix', 'is_valid', 'set_intrinsics', 'width']
    # i = o3d.camera.PinholeCameraIntrinsic(w, h, fx, fy, w/2, h/2)
    # print(i)
    # print(i.intrinsic_matrix)

    # # camera parameters, Contains both intrinsic and extrinsic pinhole camera parameters.
    # # classopen3d.camera.PinholeCameraParameters
    # p = o3d.camera.PinholeCameraParameters()
    # print(p)
    # p.intrinsic = i
    # print(p.intrinsic.intrinsic_matrix)

    # # p.extrinsic = 



