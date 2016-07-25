from setuptools import setup, find_packages


setup(
    name='bugvoyage',
    author='magniff',
    description=(
        'My "hypothesis" based survey for CPython`s internal/stdlib bugs.',
    ),
    license='MIT',
    url='https://github.com/magniff/bugvoyage',
    version='0.1',
    install_requires=["hypothesis", "pytest"],
    packages=find_packages(),
    zip_safe=False,
)
