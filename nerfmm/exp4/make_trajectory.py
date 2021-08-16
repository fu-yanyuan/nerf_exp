import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
import os

# load data
pcd = o3d.io.read_triangle_mesh("data/bun_zipper.ply")
pcd.compute_vertex_normals()
print(pcd) # print the number of points.

'''trajectory settings'''
# L = []
# for x in range(30):
#     r = [0, 0]
#     r[0] = -3
#     L.append(r)
# for x in range(10):
#     r = [0, 0]
#     r[1] = 15
#     L.append(r)
# for x in range(30):
#     r = [0, 0]
#     r[0] = 10
#     L.append(r)
# for x in range(20):
#     r = [0, 0]
#     r[1] = 5
#     L.append(r)
# for x in range(50):
#     r = [0, 0]
#     r[0] = 5
#     L.append(r)

T1 = []
T2 = []
for t in range(4):
    T1.append([0,-0.0035,0])
    T2.append([-6,0])
for t in range(4):
    T1.append([0,0,0.0025])
    T2.append([0,10])
for t in range(10):
    T1.append([0,0.002,0])
    T2.append([4,0])
for t in range(4):
    T1.append([0,0,0.0055])
    T2.append([0,10])
for t in range(8):
    T1.append([0,-0.001,0])
    T2.append([-5,0])

def custom_draw_geometry_with_rotation(pcd):
    trajectory = o3d.camera.PinholeCameraTrajectory()
    trajectory_parameters = []

    custom_draw_geometry_with_rotation.index = 0
    if not os.path.exists("exp2/"):
        os.makedirs("exp2/")

    def rotate_view(vis):
        if custom_draw_geometry_with_rotation.index < len(T1):
            image = vis.capture_screen_float_buffer(False) # to get the current image
            plt.imsave("exp2/{:05d}.png".format(custom_draw_geometry_with_rotation.index),\
                    np.asarray(image), dpi = 1)

            '''rotation'''
            # ctr = vis.get_view_control() # it seems that this line is redundant
            ctr.camera_local_rotate(T2[custom_draw_geometry_with_rotation.index][0],T2[custom_draw_geometry_with_rotation.index][1])
            # ctr.rotate(L[custom_draw_geometry_with_rotation.index][0],L[custom_draw_geometry_with_rotation.index][1]) # check camera_local_rotate

            '''translate'''
            ctr.camera_local_translate(T1[custom_draw_geometry_with_rotation.index][0],T1[custom_draw_geometry_with_rotation.index][1],T1[custom_draw_geometry_with_rotation.index][2])

            cam_parameters = ctr.convert_to_pinhole_camera_parameters()
            trajectory_parameters.append(cam_parameters)
            # print(cam_parameters.intrinsic.intrinsic_matrix )
            custom_draw_geometry_with_rotation.index = custom_draw_geometry_with_rotation.index + 1 

        # print(custom_draw_geometry_with_rotation.index)
        return False

    vis = o3d.visualization.Visualizer()
    # vis.create_window()
    vis.create_window(width=512,height=512)
    vis.add_geometry(pcd)
    ctr = vis.get_view_control()
    ctr.set_zoom(zoom=0.8)
    vis.register_animation_callback(rotate_view)
    vis.run()
    vis.destroy_window()

    '''save trajectory'''
    trajectory.parameters = trajectory_parameters
    o3d.io.write_pinhole_camera_trajectory("exp2/trj.json", trajectory)
    # print(len(trajectory.parameters))
    # print(trajectory.parameters[0].intrinsic.intrinsic_matrix)


if __name__ == "__main__":

    print(len(L))
    # help(o3d.visualization.draw_geometries_with_animation_callback)
    custom_draw_geometry_with_rotation(pcd)