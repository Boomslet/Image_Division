from setuptools import setup, find_packages
from codecs import open
from os import path


setup(
    name='Image_Division',

    version='1.0.1',

    description='A small script to divide image files into their four quarters',

    # The project's main homepage.
    url='https://github.com/Boomslet/Image_Division',

    # Author details
    author='Mark Boon',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='image PIL divide quarters',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    install_requires=['Pillow'],
)
