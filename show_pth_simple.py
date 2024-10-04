import torch
import numpy as np
import csv

# ファイルのパス
# file_path = '/home/my_output/my_pillar_logs/pillar_logs_160_git_ori/checkpoints/epoch_20.pth'
file_path = '/home/my_output/my_pillar_logs/10epo/checkpoints/epoch_1.pth'
# file_path = '/home/pretrained/epoch_160.pth'

# ファイルを読み込む
checkpoint = torch.load(file_path)

weight_tensor = checkpoint['pillar_encoder.conv.weight']
weight_numpy = weight_tensor.cpu().numpy()

# テンソルの中身の値を表示する
print(weight_numpy.shape)

# csv_file = 'weights_1_np.csv'
# with open(csv_file, 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(weight_numpy)

# # 中身を確認する
# for key in checkpoint.keys():
#     print(f"Key: {key}, Type: {type(checkpoint[key])}, Shape: {checkpoint[key].shape}")
