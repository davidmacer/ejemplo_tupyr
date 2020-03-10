from setuptools import setup, find_packages

setup(
    name='horuga',
    version='0.1',
    packages=find_packages(),
    include_packages_data=True,
    install_requires=[
        'typer',
    ],
    entry_points={
        "console_scripts": [
        "yourscript= src.main:app"
        ]
    }
)