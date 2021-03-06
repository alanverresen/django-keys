#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Used to install package and all of its dependencies.

from os import path
from setuptools import setup
from setuptools import find_packages


def read_file_contents(relative_filepath):
    """ Returns contents of a textfile as a single string.

    :param str relative_filepath: path of file relative to repository root

    :return: contents of textfile
    :rtype: str
    """
    dir_path = path.abspath(path.dirname(__file__))
    abs_path = path.join(dir_path, relative_filepath)
    with open(abs_path, encoding="utf-8") as f:
        contents = f.read()
    return contents


def get_package_requirements():
    """ Used to read requirements from requirements.txt file.

    :return: list of requirements
    :rtype: list
    """
    requirements = []
    for line in read_file_contents("requirements.txt").splitlines():
        line = line.strip()
        if line == "" or line.startswith("#"):
            continue
        requirements.append(line)
    return requirements


setup(

    name="django-keys",
    url="https://github.com/alanverresen/django-keys",
    version="1.0.4",
    python_requires=">=3.7",
    license="MIT",

    description="Python package and CLI tool for generating and handling secret keys used by Django applications.",
    long_description=read_file_contents("README.rst"),
    long_description_content_type="text/x-rst",

    author="Alan Verresen",
    author_email="django-keys@alanverresen.com",

    packages=find_packages(exclude=("tests",)),
    install_requires=get_package_requirements(),
    include_package_data=True,

    test_suite="tests",
    tests_require=[
        "pytest",
    ],

    keywords=[
        "Django", "secret", "secrets", "SECRET_KEY",
    ],


    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",

        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",

        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
    ],

)
