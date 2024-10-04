#GPUが使用可能かどうかを確認
# True1なら使用可能

#GPU番号を表示 インデックスは0はじまり
import torch
print("GPU availablity:", torch.cuda.is_available)

print( "GPU Index:",torch.cuda.current_device())