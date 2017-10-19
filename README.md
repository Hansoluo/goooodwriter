这种结构有 4 个顶级文件夹：
* Flask 程序一般都保存在名为 app 的包中；
* migrations 文件夹包含数据库迁移脚本；
* 单元测试编写在 tests 包中；
* venv 文件夹包含 Python 虚拟环境。

同时还创建了一些新文件：
* requirements.txt 列出了所有依赖包，便于在其他电脑中重新生成相同的虚拟环境；
* config.py 存储配置；
* manage.py 用于启动程序以及其他的程序任务。
