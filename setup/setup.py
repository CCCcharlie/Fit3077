import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # 如果您的应用程序是一个GUI应用程序，则设置base为"Win32GUI"

setup(
    name="YourAppName",
    version="1.0",
    description="Your application description",
    executables=[Executable("your_script.py", base=base)],  # 将"your_script.py"替换为您的Python脚本文件名
)
