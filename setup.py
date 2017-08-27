from setuptools import setup, find_packages
import youdao_simple

setup(
    name = 'youdao_simple',
    version = youdao_simple.__version__,
    author = 'Dongliang Mu',
    author_email = 'mudongliangabcd@gmail.com',
    url = "https://github.com/mudongliang/youdao-python",
    packages = ['youdao_simple',],
    license='GPL v3.0',
    classifiers = [
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    description = 'Youdao Python',
    long_description = open('README').read(),
    entry_points = {
        'console_scripts': [
            'youdao = youdao_simple.youdao:main',
        ],
    },
)
