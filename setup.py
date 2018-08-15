from setuptools import setup, find_packages


setup(
    name='ecsvdb',
    version='1.0',
    install_requires=[
        'read_and_close'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ecsvdb-client = ecsvdb.client_bin:run'
        ]
    }
)
