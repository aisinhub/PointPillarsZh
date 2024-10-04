import torch

# 仮のデータとして pillars_z_tensor_2d を定義する（3x2の行列と仮定）
pillars_z_tensor_2d = torch.tensor([[1.1, 2], [3, 4], [5, 6]])
print(pillars_z_tensor_2d)
print(pillars_z_tensor_2d.shape)

# num_points を 5 とする
num_points = 5

# 1x5のテンソルを作成し、2次元のテンソルにする
ones_tensor = torch.ones(1, num_points).unsqueeze(0)

# 3次元のテンソルに拡張したいので、pillars_z_tensor_2d に新しい次元を追加する
# そして、行列積を計算する
# pillars_z_tensor_3d = pillars_z_tensor_2d.unsqueeze(2).matmul(ones_tensor)

new_tensor = pillars_z_tensor_2d.unsqueeze(0).repeat(2, 1, 1)
pillars_z_tensor_3d = new_tensor.permute(1, 0, 2)

print(pillars_z_tensor_3d)
print(pillars_z_tensor_3d.shape)