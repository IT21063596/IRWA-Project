from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = 'WD'
SRC_REOP = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name = SRC_REOP,
    version = '0.0.1',
    author = AUTHOR_NAME,
    author_email='wdewpura@gmail.com',
    description= 'A small example package for movie recommendation',
    long_description= long_description,
    long_description_content_type = 'text/markdown',
    package = [SRC_REOP],
    python_requires = '>=3.7',
    install_requires = LIST_OF_REQUIREMENTS,
)