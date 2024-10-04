# 実行前に，保存用ディレクトリは作成しておくこと
# python3 kitti2ply.py /home/data/training/velodyne/000000.bin /home/data/my_ply/training/velodyne
#というふうに使う

import numpy as np
import sys
import open3d as o3d

args = sys.argv

bin_file = args[1]
save_file = args[2]

bin_file_tmp = bin_file.split("/")
file_name = bin_file_tmp[-1].split(".")[-2]

lidar_point = np.fromfile(bin_file, dtype=np.float32).reshape((-1,4)) #binをnumpyで格納

xyz = np.array(lidar_point[:,0:3]) #XYZ情報のみ抽出

pcd = o3d.geometry.PointCloud() #以下，保存のための作業
pcd.points = o3d.utility.Vector3dVector(xyz)
o3d.io.write_point_cloud(save_file+"/"+file_name+".ply", pcd)