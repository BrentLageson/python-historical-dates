"""
This module provides setup info for python
"""
from setuptools import setup, find_packages

# Read the contents of your README file
with open('README.md', mode='r', encoding='utf-8') as readme_file:
    long_description = readme_file.read()

setup(
    name='historicaldates',
    version='1.0.0',
    author='Brent Lageson',
    author_email='brent.lageson@gmail.com',
    description='Python library for handling BCE and CE dates.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/BrentLageson/python-historical-dates',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
