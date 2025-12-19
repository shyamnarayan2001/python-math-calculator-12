"""
Setup configuration for Python Math Calculator package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="python-math-calculator",
    version="1.0.0",
    author="Narayan Krishnamurthy Shyam",
    author_email="shyamnarayan2001@gmail.com",
    description="A simple calculator library for basic mathematical operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shyamnarayan2001/python-math-calculator-12",
    py_modules=["calculator"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
    },
)
