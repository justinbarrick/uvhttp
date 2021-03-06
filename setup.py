from setuptools import setup
import os

requirements = os.path.join(os.path.dirname(__file__), 'requirements.txt')

setup(
    name='uvhttp',
    version='1.18',
    description='High performance Python HTTP client',
    url='https://github.com/justinbarrick/uvhttp',
    package_data={'uvhttp': ['example.pem']},
    include_package_data=True,
    packages=['uvhttp'],
    install_requires=[ r.rstrip() for r in open(requirements).readlines() ]
)
