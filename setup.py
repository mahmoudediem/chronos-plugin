from setuptools import setup, find_packages

setup(
    name="chronos-plugin",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "git+https://github.com/mahmoudediem/shareddep.git@v2.0.0#egg=shareddep"
    ],
)