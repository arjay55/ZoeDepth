import setuptools
from codecs import open

exec(open('zoedepth/version.py').read())

setuptools.setup(
    name="zoedepth",
    version='0.5.0',
    author="Bhat, Shariq Farooq and Birkl, Reiner and Wofk, Diana and Wonka, Peter and Müller, Matthias",
    description="A short description of your package",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
    ],
)