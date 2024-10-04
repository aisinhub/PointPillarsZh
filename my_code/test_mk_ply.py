# coding: utf-8
# import open3d as o3d
# import numpy as np

# world = [[0.0, 0.0, 0.0], [0.0, 0.05, 0.0], [0.0, 0.1, 0.0], [0.05, 0.0, 0.0], [0.05, 0.05, 0.0], [0.05, 0.1, 0.0], [0.1, 0.0, 0.0], [0.1, 0.05, 0.0], [0.1, 0.1, 0.0], [0.0, 0.0, 0.05], [0.0, 0.05, 0.05], [0.0, 0.1, 0.05], [0.05, 0.0, 0.05], [0.05, 0.05, 0.05], [0.05, 0.1, 0.05], [0.1, 0.0, 0.05], [0.1, 0.05, 0.05], [0.1, 0.1, 0.05]]

# xyz = np.array(world)
# pcd = o3d.geometry.PointCloud()
# pcd.points = o3d.utility.Vector3dVector(xyz)
# o3d.io.write_point_cloud("test.ply", pcd)

import sys
import open3d as o3d
args = sys.argv

save_path = args[1]
file_name = "bbb"
_save_fullpath = save_path+"/"+file_name+".ply"

print(_save_fullpath)


for i in range(1, 11):
    file_name = f'{i:06}'
    print(file_name)