from setuptools import setup, find_packages

setup(
     packages = find_packages(),
     data_files = [('/etc/toutetu', ['toutetu/food.conf'])],
)
