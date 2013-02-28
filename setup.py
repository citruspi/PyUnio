from distutils.core import setup

long_description = \
'''
This is a Python implementation of Tolga Tezel's Node.js project unio_. 

Documentation and usage can be found on the pyunio_ page on Github.

.. _unio: http://github.com/ttezel/unio
.. _pyunio: http://github.com/citruspi/pyunio
'''

setup(
	name='pyunio',
	version='0.1.1',
	author='Mihir Singh',
	author_email='me@mihirsingh.com',
	packages=['pyunio'],
	url='http://pypi.python.org/pypi/pyunio/',
	license='MIT License',
	description='Python implementation of unio.',
	long_description=long_description,
	install_requires=[
						'requests',
						'requests_oauthlib'
					 ]
)