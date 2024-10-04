import open3d as o3d
import torch

# 点群データの読み込み
point_cloud = o3d.io.read_point_cloud("/home/data/kitti_data/teapotOut.ply")  # あなたの点群データのパスを指定してください

# Open3DのPointCloudからNumpy配列に変換
xyz_np = torch.tensor(point_cloud.points)
print('-------xyz_np')
print(xyz_np.shape)

total_points = xyz_np.shape[0] # テンソルのサイズを取得
group_size = 100  # 1グループあたりの点の数
num_groups = total_points // group_size # グループ数を計算
remainder = total_points % group_size  # 最後のグループの点の数

# P * 100 * 3のテンソルを生成
tensor_groups = []
for i in range(num_groups):
    start_idx = i * group_size
    end_idx = start_idx + group_size
    group = xyz_np[start_idx:end_idx]  # 1グループ分の点群データ
    tensor_groups.append(group.unsqueeze(0))  # テンソルに変換し、リストに追加

if remainder > 0:
    last_group = xyz_np[-remainder:]  # 最後のグループの点群データを選択
    padding = torch.zeros(group_size - remainder, 3)  # あまりの部分をゼロパディング
    last_group_padded = torch.cat([last_group, padding], dim=0)  # ゼロパディングされた最後のグループ
    tensor_groups.append(last_group_padded.unsqueeze(0))  # テンソルに変換し、リストに追加

grouped_tensor = torch.cat(tensor_groups, dim=0)
print(grouped_tensor.shape)

# num_elements = grouped_tensor.numel()/3
# print('-------num_elements')
# print(num_elements)

print(grouped_tensor[414,:,2])
