import numpy as np
import torch 

# 3次元のテンソルを作成
# tensor = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

tensor1 = torch.tensor([[[1, 1, 1, 1], [2, 2, 2, 2]], [[3, 3, 3, 3], [4, 4, 4, 4]]])
tensor2 = torch.tensor([[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]], [[5, 6, 7, 8], [5, 6, 7, 8], [5, 6, 7, 8]]])
tensor3 = torch.tensor([[[1, 2, 3, 4, 99], [1, 2, 3, 4, 99], [1, 2, 3, 4, 99]], [[5, 6, 7, 8, 99], [5, 6, 7, 8, 99], [5, 6, 7, 8, 99]]])
tensor3_ext = tensor3[:,0,:]

result = torch.mean(tensor2[:, :, :3].float(), dim=1)
print(result.size())
print(result)
