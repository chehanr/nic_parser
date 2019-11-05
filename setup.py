from setuptools import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license_file = f.read()

setup(
    name='nic_parser',
    version='0.2.0',
    description='A python library to parse Sri Lankan national identity card numbers',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Chehan Ratnasiri',
    author_email='chehan.rat@gmail.com',
    url='https://github.com/chehanr/nic_parser',
    license="GNU General Public License",
    packages=['nic_parser'],
    install_requires=['', ],
    download_url='https://github.com/chehanr/nic_parser/archive/0.1.0.tar.gz',
    keywords=['nic', 'parser', 'sri-lanka'],
    classifiers=[],
)
