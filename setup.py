
from setuptools import setup

try:
    long_desc = open('README.md').read()
except IOError:
    long_desc = ''

setup(
    name='django-riemann',
    version='0.0.2',
    url='https://github.com/honza/django-riemann',
    install_requires=[
        'bernhard'
    ],
    description='Send logging data to Riemann',
    long_description=long_desc,
    author='Honza Pokorny',
    author_email='me@honza.ca',
    maintainer='Honza Pokorny',
    maintainer_email='me@honza.ca',
    packages=['riemann'],
    include_package_data=True
)
