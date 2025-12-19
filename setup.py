"""Setup configuration for python-math-calculator package"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="python-math-calculator",
    version="0.1.0",
    author="Shyam Narayan",
    author_email="shyamnarayan2001@gmail.com",
    description="A simple calculator for basic math operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shyamnarayan2001/python-math-calculator-12",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "pylint>=2.17.0",
            "black>=23.7.0",
            "flake8>=6.1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "calculator=calculator:main",
        ],
    },
)
