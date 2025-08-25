import torch

device = "mps" if torch.backends.mps.is_available() else "cpu"
print("Using device:", device)

# 创建随机矩阵
a = torch.rand(1000, 1000, device=device)
b = torch.rand(1000, 1000, device=device)

# 矩阵乘法
c = torch.matmul(a, b)
print("Matrix multiplication done. Shape:", c.shape)
