#!/usr/bin/env python
from setuptools import dist
dist.Distribution().fetch_build_eggs(['setuptools_rust'])
from setuptools import setup
from setuptools_rust import RustExtension, Binding

setup(
    name="andrew_fib_rs",
    version="0.1.0",
    rust_extensions=[RustExtension(
        ".andrew_fib_rs.andrew_fib_rs",
        path="Cargo.toml", 
        binding=Binding.PyO3)],
    packages=["andrew_fib_rs"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Rust",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
    ],
    zip_safe=False,
)
