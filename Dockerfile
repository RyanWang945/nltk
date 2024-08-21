FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 安装 NLTK
RUN pip install nltk

# 下载所有 NLTK 数据
RUN python -m nltk.downloader -d /usr/local/share/nltk_data all

# 复制你的应用程序源码（如果有）
# COPY . .

# 设置默认命令（可选）
CMD ["python"]
