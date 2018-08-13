from setuptools import setup, find_packages


setup(
    name='ecsvdb',
    version='1.0',
    install_requires=[],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ecsvdb = ecsvdb.bin:run'
        ]
    }
)
