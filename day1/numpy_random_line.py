import numpy as np
import matplotlib.pyplot as plt

# 生成 0-10 间 100 个点
x = np.linspace(0, 10, 100)
y = np.sin(x) + 0.2 * np.random.randn(100)  # 加一点随机噪声

plt.plot(x, y, label='Noisy Sine')
plt.title("Day 1: Random Sine Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
