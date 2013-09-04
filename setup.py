from setuptools import setup

setup(
    name='eutils',
    version='0.2.1',
    url='https://stash.ncbi.nlm.nih.gov/projects/WT/repos/python-eutils',
    author='Klortho',
    author_email='voldrani@gmail.com',
    packages=[
        'eutils',
    ],
    install_requires=['requests']
)
