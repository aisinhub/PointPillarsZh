import torch


print(torch.__version__)

a = torch.rand(1, 1000, 1000, 1000).to("cuda")


if torch.cuda.is_available():
    # プログラム実行前の最大アロケートメモリを取得
    peak_allocated = torch.cuda.max_memory_allocated()
    # プログラム実行中にキャッシュされた最大メモリを取得
    peak_cached = torch.cuda.max_memory_cached()
    
    print(f"Peak Allocated Memory: {peak_allocated} bytes")
    print(f"Peak Cached Memory: {peak_cached} bytes")
else:
    print("CUDAデバイスは使用不可です")

import GPUtil
gpus = GPUtil.getGPUs()
for gpu in gpus:
    print(f"ID: {gpu.id} / {gpu.name}")
    print(f"Memory Total: {gpu.memoryTotal} MB")
    print(f"Memory Used: {gpu.memoryUsed} MB")
    print(f"Memory Free: {gpu.memoryFree} MB")
    print(f"Memory Utilization: {gpu.memoryUtil * 100} %")
    print(f"GPU Utilization: {gpu.load * 100} %")
    print("\n")