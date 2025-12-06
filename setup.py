from setuptools import setup, find_packages

setup(
    name="chronos-plugin",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "shareddep"   # Only package name here — NO Git URLs
    ],
)
