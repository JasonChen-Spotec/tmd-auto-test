1. 自动登录
2. 环境变量控制不同环境地址
3. resultClient封装
4. 测试环境执行的注解
5. 测试报告

在 Python 项目中，可以通过以下几种方式来设置环境变量：

在代码中直接设置：
python
import os

# 设置环境变量
os.environ['MY_VAR'] = 'my_value'

# 获取环境变量的值
value = os.getenv('MY_VAR')
在命令行或启动脚本中设置环境变量： 在运行 Python 项目之前，可以在命令行或启动脚本中设置环境变量，例如：
$ export MY_VAR=my_value
$ python my_script.py
以上是设置 Python 项目中环境变量的几种常用方法，您可以根据具体情况选择合适的方式来设置环境变量。
