from setuptools import setup
from setuptools import find_packages

setup(
    name='jetstream',
    version='0.1.2',
    packages=['jetstream'],
    url='https://github.com/samapriya/jetstream-unofficial-addon',
    install_requires=['requests >= 2.18.4'],
    license='Apache 2.0',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: GIS',
    ),
    author='Samapriya Roy',
    author_email='samapriya.roy@gmail.com',
    description='Jetstream Atmosphere VM(s) Unofficial Addons',
    entry_points={
        'console_scripts': [
            'jetstream=jetstream.jetstream:main',
        ],
    },
)
