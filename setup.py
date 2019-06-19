from setuptools import setup, find_packages
import os

setup(
     packages = find_packages(),
     data_files = [(os.path.expanduser('~/.toutetu'), ['toutetu/food.conf'])],
)
