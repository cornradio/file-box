## 环境准备

```
pip install flask flask_cors
```

recommand version:

```
Python 3.11.10
Flask 3.1.0
Werkzeug 3.1.3
```

## 修改配置
port.js 文件 修改下列配置，保证可以访问到后端api

```
let baseurl = "http://xxx:3000/box1"
```

## 启动程序
1. 主页放到 ngxin 目录下
2. 进入 filebox-api 目录下使用 命令启动：

```
flask run --host 0.0.0.0 -p3000 --debug
```
## 截图
<img width="1100" alt="image" src="https://github.com/user-attachments/assets/86da3bc5-3849-4ca5-9cad-3de0f218ded9">



