from distutils.core import setup
from setuptools import find_packages
import os

this = os.path.dirname(__file__)

packages = find_packages()
assert packages

# read version from the package file.
version_str = "0.0.2"
with (open(os.path.join(this, "hummingbird/__init__.py"), "r")) as f:
    line = [_ for _ in [_.strip("\r\n ") for _ in f.readlines()] if _.startswith("__version__")]
    if len(line) > 0:
        version_str = line[0].split("=")[1].strip('" ')

README = os.path.join(os.getcwd(), "README.md")
with open(README) as f:
    long_description = f.read()
    start_pos = long_description.find("## Introduction")
    if start_pos >= 0:
        long_description = long_description[start_pos:]

setup(
    name="hummingbird-ml",
    version=version_str,
    description="Convert trained traditional machine learning models into tensor computations",
    license="MIT License",
    author="Microsoft Corporation",
    author_email="hummingbird-dev@microsoft.com",
    url="https://github.com/microsoft/hummingbird",
    packages=packages,
    include_package_data=True,
    install_requires=["numpy>=1.15", "torch>=1.4.0", "onnxconverter-common>=1.6.0", "scikit-learn==0.22.1"],
    extras_require={
        "tests": ["flake8", "pytest", "coverage", "pre-commit"],
        "docs": ["pdoc"],
        "extra": [
            # The need each for these depends on which libraries you plan to convert from
            "xgboost==0.90",
            "lightgbm>=2.2",
        ],
    },
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.5",
)
