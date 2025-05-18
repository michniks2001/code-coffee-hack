from setuptools import setup, find_packages

setup(
    name="apiport",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        'console_scripts': [
            'apiport=apiport.__main__:main',
        ],
    },
    python_requires='>=3.6',
    description="CLI tool for managing API secrets",
)
