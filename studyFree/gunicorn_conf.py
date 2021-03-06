# gunicorn/django  服务监听地址、端口
bind = '0.0.0.0:8210'

# gunicorn worker 进程个数，建议为： CPU核心个数 * 2 + 1
workers = 3

# gunicorn worker 类型， 使用异步的event类型IO效率比较高
worker_class = "gevent"

# 日志文件路径
errorlog = "./log/error.log"
accesslog = './log/access.log' #正常时的log路径
loglevel = "info"

import os
import sys

cwd = os.getcwd()
sys.path.append(cwd)
