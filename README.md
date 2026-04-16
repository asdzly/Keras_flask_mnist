# Keras_flask_mnist
基于 TensorFlow2.0 （Keras） + Flask 的 Mnist 手写数字集识别系统

- 演示地址
```
http://101.42.235.106:8835/ （公网IP访问）
http://paulson.free.idcfengye.com/ （内网穿透 ngrox 域名访问） 可以看下面我的博客链接地址  # 暂不支持
http://http://101.42.235.106:8836   （前后端分离 vue版访问路径--原服务器下掉了，新的服务还没部署）
```

- 下载

### 部署
- 下载
```c
git clone https://github.com/ybsdegit/Keras_flask_mnist.git
```
- 安装依赖
```
pip install -r requirements.txt
```

# 运行

- 启动服务
```
python app.py
```
本地启动访问地址为：`http://localhost:3335/`

- 训练
源码中也包含训练好的模型 `model.h5`,测试集成功率99.9，也可以自行训练。
```
python model/train.py
```

### 博客
```
https://blog.csdn.net/qq_38534107/article/details/103565899 （mnist）
https://blog.csdn.net/qq_38534107/article/details/106009215 （内网穿透）
```
