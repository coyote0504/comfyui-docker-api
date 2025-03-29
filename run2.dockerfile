FROM nvidia/cuda:12.4.0-devel-ubuntu22.04

# 设置非交互式前端
ENV DEBIAN_FRONTEND=noninteractive

# 设置工作目录
WORKDIR /app

# 安装基本依赖
RUN apt-get update && apt-get install -y \
    git \
    wget \
    curl \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    ffmpeg \
    software-properties-common \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 安装Python 3.12
RUN add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.12 python3.12-dev python3.12-venv && \
    curl -sS https://bootstrap.pypa.io/get-pip.py | python3.12 && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 1 && \
    update-alternatives --install /usr/bin/python python /usr/bin/python3.12 1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 创建Python虚拟环境
RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# 更新pip
RUN pip install --upgrade pip

# 克隆ComfyUI仓库
RUN git clone https://github.com/comfyanonymous/ComfyUI.git /app/ComfyUI

# 进入ComfyUI目录并安装依赖
WORKDIR /app/ComfyUI

# 安装PyTorch和torchvision与CUDA 12.1兼容的最新版本
RUN pip install torch==2.5.1 torchvision==0.20.1 --index-url https://download.pytorch.org/whl/cu121

# 安装ComfyUI依赖
RUN pip install -r requirements.txt

# 安装额外常用依赖
RUN pip install matplotlib opencv-python scikit-image transformers

# 创建模型和输出目录
RUN mkdir -p /app/ComfyUI/models/checkpoints
RUN mkdir -p /app/ComfyUI/models/vae
RUN mkdir -p /app/ComfyUI/models/loras
RUN mkdir -p /app/ComfyUI/models/controlnet
RUN mkdir -p /app/ComfyUI/models/clip
RUN mkdir -p /app/ComfyUI/models/upscale_models
RUN mkdir -p /app/ComfyUI/output

# 设置工作目录
WORKDIR /app/ComfyUI

# 暴露端口
EXPOSE 8188

# 启动ComfyUI
CMD ["python", "main.py", "--listen", "0.0.0.0", "--port", "8188"]