from setuptools import setup, find_packages

setup(
	name='assignment1',
	version='1.0',
	author='Rahul Talari',
	authour_email='rtalari@ufl.edu',
	packages=find_packages(exclude=('tests', 'docs')),
	setup_requires=['pytest-runner'],
	tests_require=['pytest']	
)
