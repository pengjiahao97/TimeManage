from setuptools import setup

setup(
    name='TimeManager',
    version='0.0.1',
    description='auto generate excel for time manage',
    license='MIT License',
    install_requires=["openpyxl"],
    packages=['TimeManager'],
    include_package_data=True,
    author='Patrick Peng',
    author_email='pengjiahao97@gmail.com',
    url='https://github.com/pengjiahao97/TimeManage',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
