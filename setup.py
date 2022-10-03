#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = []

test_requirements = [
    "pytest>=3.10",
]

setup(
    author="Tr4shL0rd",
    author_email="ketil04@gmail.com",
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.10",
    ],
    description="get_video_length gets the length of a video",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="get_video_length",
    name="get_video_length",
    packages=find_packages(include=["get_video_length", "get_video_length.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/Tr4shL0rd/get_video_length",
    version="0.1.0",
    zip_safe=False,
)
