#!/usr/bin/env python
from setuptools import setup, find_packages
import gpp

setup(
    name="ajava_pyext_functions",
    version=gpp.__version__,
    author="aJava",
    author_email="gaolious@gmail.com",
    description="personally, python extension functions",
    url="https://github.com/Gaolious/gpp",
    packages=find_packages(include=('gpp',), exclude=('__pycache__',)),
    include_package_data=True,
    python_requires=">=3.9",
    install_requires=["pytz"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
