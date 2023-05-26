import setuptools
from codecs import open

exec(open('timm/version.py').read())

setuptools.setup(
    name="zoedepth",
    version=__version__,
    author="Bhat, Shariq Farooq and Birkl, Reiner and Wofk, Diana and Wonka, Peter and Müller, Matthias",
    description="A short description of your package",
    packages=setuptools.find_packages(),
    install_requires=[
    ],
)