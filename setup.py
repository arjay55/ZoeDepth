import setuptools
from codecs import open

exec(open('zoedepth/version.py').read())

setuptools.setup(
    name="zoedepth",
    version=__version__,
    author="Bhat, Shariq Farooq and Birkl, Reiner and Wofk, Diana and Wonka, Peter and Müller, Matthias",
    description="A short description of your package",
    packages=setuptools.find_packages(),
    install_requires=[
    ],
    package_data={'zoedepth': ['zoedepth/*.json'],
                  'zoedepth': ['zoedepth_nk/*.json']},
)