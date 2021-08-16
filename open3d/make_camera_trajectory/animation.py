import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
import os

# load data
pcd = o3d.io.read_triangle_mesh("data/bun_zipper.ply")
pcd.compute_vertex_normals()
print(pcd) # print the number of points.

def custom_draw_geomery_with_camera_trajectory(pcd):
    custom_draw_geomery_with_camera_trajectory.index = -1
    custom_draw_geomery_with_camera_trajectory.trajectory =\
        o3d.io.read_pinhole_camera_trajectory(
            "fullsc.json"
        )
    custom_draw_geomery_with_camera_trajectory.vis = o3d.visualization.Visualizer()

    def move_forward(vis):
        # This function is called within the o3d.visualization.Visualizer::run() loop
        # The run loop calls the function, then re-render
        # So the sequence in this function is to:
        # 1. Capture frame
        # 2. index++, check ending criteria
        # 3. Set camera
        # 4. (Re-render)
        ctr = vis.get_view_control()
        glb = custom_draw_geomery_with_camera_trajectory
        glb.index = glb.index + 1
        if glb.index < len(glb.trajectory.parameters):
            ctr.convert_from_pinhole_camera_parameters(
                glb.trajectory.parameters[glb.index])
        else:
            custom_draw_geomery_with_camera_trajectory.vis.\
                    register_animation_callback(None)
        return False
    
    vis = custom_draw_geomery_with_camera_trajectory.vis
    vis.create_window()
    vis.add_geometry(pcd)
    vis.register_animation_callback(move_forward)
    vis.run()
    vis.destroy_window()


if __name__ == "__main__":
    custom_draw_geomery_with_camera_trajectory(pcd)

