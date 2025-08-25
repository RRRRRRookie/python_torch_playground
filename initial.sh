#!/bin/bash
set -e

echo ">>> 使用 Python 版本:"
python3 --version

# 建议先升级 pip
echo ">>> 升级 pip..."
python3 -m pip install --upgrade pip setuptools wheel

# 安装科学计算 & 可视化基础库
echo ">>> 安装 numpy / pandas / matplotlib / seaborn / scikit-learn..."
pip install numpy==1.26.4 pandas==2.2.2 matplotlib==3.9.0 seaborn==0.13.2 scikit-learn==1.5.0

# 安装 Jupyter 相关
echo ">>> 安装 Jupyter 环境..."
pip install jupyter==1.0.0 notebook==7.2.1 ipykernel==6.29.4

# 安装常用工具
echo ">>> 安装 tqdm / requests..."
pip install tqdm==4.66.4 requests==2.32.3

# ✅ 专门为 M1/M2 芯片安装 PyTorch + MPS 支持
echo ">>> 安装 PyTorch (MPS 版本, 适配 Apple Silicon)..."
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

echo ">>> 所有依赖安装完成 ✅"
