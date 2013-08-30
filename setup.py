from setuptools import setup

setup(
    name='eutils',
    version=__import__('eutils').__version__,
    url='https://stash.ncbi.nlm.nih.gov/projects/WT/repos/python-eutils',
    author='Klortho',
    author_email='voldrani@gmail.com',
    py_modules=[
        'eutils',
    ],
)
