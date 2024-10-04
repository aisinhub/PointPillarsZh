import open3d as o3d
# numpyの点群データをopen3d に変換。 test_data -> numpy array (n,3)
pcd=o3d.geometry.PointCloud()
pcd.points = o3d. utility.Vector3dVector(test_data)
# 法線ベクトルの推定（KDTreeによる近傍点探索を使用）
pcd.estimate_normals(
    search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
# Open3dで可視化
#o3d.visualization.draw_geometries([pcd], point_show_normal=True)