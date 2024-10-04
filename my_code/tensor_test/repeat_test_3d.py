import torch


dummy_tensor1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('tensor1_size')
print(dummy_tensor1.shape)  # 形状を出力して確認
print('---------------')

# 元の3x2行列
dummy_tensor2 = torch.tensor([[1, 4], [2, 5], [3, 6]])
print('tensor2_size')
print(dummy_tensor2.shape)  # 形状を出力して確認
print(dummy_tensor2)
print('---------------')

# 3x4x2のテンソルに変換
expanded_tensor = dummy_tensor2.view(3, 4, 2)
print(expanded_tensor.shape)
print(expanded_tensor)


