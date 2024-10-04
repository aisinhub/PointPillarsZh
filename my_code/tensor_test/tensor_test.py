import numpy as np
import torch 

# 3次元のテンソルを作成
tensor = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

tensor1 = torch.tensor([[[1, 1, 1, 1], [2, 2, 2, 2]], [[3, 3, 3, 3], [4, 4, 4, 4]]])
tensor2 = torch.tensor([[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]], [[5, 6, 7, 8], [5, 6, 7, 8], [5, 6, 7, 8]]])
tensor3 = torch.tensor([[[1, 2, 3, 4, 99], [1, 2, 3, 4, 99], [1, 2, 3, 4, 99]], [[5, 6, 7, 8, 99], [5, 6, 7, 8, 99], [5, 6, 7, 8, 99]]])
tensor3_ext = tensor3[:,0,:]


array = np.array([[1, 2, 3], [4, 5, 6]])

# テンソルの内容を表示
# print(tensor1)
# print("---")

print(tensor3)
print("---")

print(tensor3_ext)
print("---")

# print(array)
# print("---")

# # 2つの次元が1の部分テンソル（2x2行列）を表示
# sub_tensor = tensor[0, :, :]
# sub_array = array[0, :]

# # テンソルの内容を表示
# print(sub_tensor)
# print("---")
# print(sub_array)

#center = torch.sum(tensor1)
center2 = torch.sum(tensor2[:, :, :], dim=1, keepdim=True)
npoints_per_pillar = torch.tensor([3])
center3 = torch.sum(tensor3[:, :, :3], dim=1, keepdim=True) / npoints_per_pillar[:, None, None] # (p1 + p2 + ... + pb, num_points, 3)
center3_ext = center3[:,0,:]

concat = torch.cat([tensor3_ext, center3_ext], dim=-1)

print(center3)
print("---")
print(center3.size())
print("---")
print(center3_ext)
print("---")
print(center3_ext.size())
print("---")
print(concat)
print("---")
print(concat.size())
print("---")
