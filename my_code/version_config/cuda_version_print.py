#現在のPyTorch環境で利用可能なCUDAバージョンを表示

import torch

print("CUDA バージョン:", torch.version.cuda)

# 同じ処理内容
#cuda_version = torch.version.cuda
#print("CUDA バージョン:", cuda_version)
