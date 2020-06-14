import os
from setuptools import setup

DIR = os.path.dirname(os.path.abspath(__file__))


def read_file(filename):
    """读取文件"""
    file_abs = os.path.join(DIR, filename)
    with open(file_abs, mode="r", encoding="utf-8") as f:
        return f.read()


def read_requirements(filename):
    """获取依赖"""
    contents = read_file(filename)
    return [pkg for pkg in contents.splitlines() if not pkg.startswith("#")]


setup(
    name='TimeManager',
    python_requires='>=3.6.0',
    version='0.0.1',
    description='generate excel for time manage',
    long_description=read_file('README.md'),  # 读取的Readme文档内容
    long_description_content_type="text/markdown",  # 指定包文档格式为markdown
    license='MIT License',
    packages=[
        'TimeManager'
    ],
    install_requires=read_requirements("requirements.txt"),  # 指定需要安装的依赖
    include_package_data=True,
    author='Patrick Peng',  # 作者相关信息
    author_email='pengjiahao97@gmail.com',
    url='https://github.com/pengjiahao97/TimeManage',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
