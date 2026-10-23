
# MDChecker 极简版
功能：递归扫描目录下Markdown，检测本地损坏图片、本地失效链接，统计标题、生成目录索引。
只校验本地资源，无第三方依赖。

## 本地运行
```bash
python main.py ./testdir
python main.py ./testdir -o report.md
# MDChecker 极简版
功能：递归扫描目录下Markdown，检测本地损坏图片、本地失效链接，统计标题、生成目录索引。
只校验本地资源，无第三方依赖。

## 本地运行
python main.py ./testdir
python main.py ./testdir -o report.md

参数：
- 第一个参数：扫描文件夹
- `-o`：可选，输出报告文件

## Docker运行
docker build -t mdcheck .
docker run -v ${PWD}\testdir:/app/testdir mdcheck /app/testdir
