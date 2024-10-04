import numpy as np
# python3 kitti2ply_loop.py /home/data/training/velodyne /home/data/all_ply/training_ply/velodyne_ply
# のように使う
import sys
import open3d as o3d
args = sys.argv

bin_dirpath = args[1]
save_dirpath = args[2]

def bint2ply(bin_filepath, save_filepath):
    
    lidar_point = np.fromfile(bin_filepath, dtype=np.float32).reshape((-1,4))

    xyz = np.array(lidar_point[:,0:3])

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(xyz)
    o3d.io.write_point_cloud(save_filepath, pcd)


for i in range(0, 7520):  # ここを変更して，PLYにするフレームの範囲の選択 ex 00000.bin~000072.bin
    file_name = f'{i:06}'
    _bin_filepath = bin_dirpath+"/"+file_name+".bin"
    _save_filepath = save_dirpath+"/"+file_name+".ply"
    bint2ply(_bin_filepath, _save_filepath)
    
    print(i)