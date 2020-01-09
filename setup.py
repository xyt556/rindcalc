import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Owen Smith",
    author_email="owen8461@protonmail.com",
    name='rindcalc',
    license="MIT",
    description='rindcalc is a python package created to calculate Landsat-8 indices.',
    version='v0.0.6',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/ocsmit/raster-indices-calc',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=['numpy', 'gdal'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: GIS',
        'Intended Audience :: Science/Research',
    ],
)
