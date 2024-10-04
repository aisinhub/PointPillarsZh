import torch


dummy_tensor1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('---------------tensor1_size')
print(dummy_tensor1.shape)  # 形状を出力して確認
dummy_tensor1_sq = dummy_tensor1.unsqueeze(-1)
print('---------------tensor1_sq_size')
print(dummy_tensor1_sq.shape)  # 形状を出力して確認


dummy_tensor2 = torch.tensor([[1.1], [2], [3]])
print('---------------tensor2_size')
print(dummy_tensor2.shape)  # 形状を出力して確認
print(dummy_tensor2)
dummy_tensor2_sq = dummy_tensor2.unsqueeze(-1)
print('---------------tensor2_sq_size')
print(dummy_tensor2_sq.shape)  # 形状を出力して確認
print(dummy_tensor2_sq)

# 3番目の軸を num_points に拡張
# expanded_tensor = dummy_tensor2.mm(torch.ones(1, 4))
expanded_tensor = dummy_tensor2_sq.expand(3,4,1)
print('---------------expand_size')
print(expanded_tensor.shape)
print(expanded_tensor)


